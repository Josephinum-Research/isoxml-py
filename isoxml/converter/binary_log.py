import struct
from datetime import time, date, datetime
from decimal import Decimal
from io import BytesIO

import pandas as pd
from dateutil import tz

import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4
from isoxml.models.ddi_entities import DDEntity

__struct_type_lut = {
    'time_of_day': 'I',
    'date': 'H',
    'position_north': 'i',
    'position_east': 'i',
    'position_up': 'i',
    'position_status': 'B',
    'pdop': 'H',
    'hdop': 'H',
    'number_of_satellites': 'B',
    'gps_utc_time': 'I',
    'gps_utc_date': 'H',
}


def __to_time(ms_sinc_midnight: int, tzinfo=None) -> time:
    hours = ms_sinc_midnight // (1000 * 60 * 60)
    minutes = (ms_sinc_midnight % (1000 * 60 * 60)) // (1000 * 60)
    seconds = (ms_sinc_midnight % (1000 * 60)) // 1000
    microseconds = ms_sinc_midnight % 1000

    return time(hour=hours, minute=minutes, second=seconds, microsecond=microseconds, tzinfo=tzinfo)


__value_conversion_lut = {
    'time_of_day': __to_time,
    'date': lambda x: date.fromtimestamp(x * 24 * 60 * 60),
    'position_north': lambda x: Decimal(x) * Decimal('1e-7'),
    'position_east': lambda x: Decimal(x) * Decimal('1e-7'),
    'position_up': lambda x: x,
    'position_status': lambda x: x,
    'pdop': lambda x: Decimal(x) * Decimal('1e-1'),
    'hdop': lambda x: Decimal(x) * Decimal('1e-1'),
    'number_of_satellites': lambda x: x,
    'gps_utc_time': lambda x: __to_time(x, tz.gettz('UTC')),
    'gps_utc_date': lambda x: date.fromtimestamp(x * 24 * 60 * 60),
}


def bin_log_to_dict(time_element: iso3.Time | iso4.Time, data: bytes) -> list[dict]:
    assert len(time_element.positions) == 1, "this not not forbidden, but i don't understand it"
    position_header = time_element.positions[0]
    record_template = {
        'time_of_day': None,
        'date': None,
        'position_north': position_header.north,
        'position_east': position_header.east,
        'position_up': position_header.up,
        'position_status': position_header.status,
        'pdop': position_header.pdop,
        'hdop': position_header.hdop,
        'number_of_satellites': position_header.number_of_satellites,
        'gps_utc_time': __value_conversion_lut['gps_utc_time'](position_header.gps_utc_time) if position_header.gps_utc_time else None,
        'gps_utc_date': __value_conversion_lut['gps_utc_date'](position_header.gps_utc_time) if position_header.gps_utc_date else None,
        'dlvs': []
    }

    rec_fix_format = '<'
    missing_attrs = []
    for k, v in record_template.items():
        if (not v or v == '') and k in __struct_type_lut:
            rec_fix_format += __struct_type_lut[k]
            missing_attrs.append(k)
    rec_fix_format += 'B'
    rec_fix_size = struct.calcsize(rec_fix_format)
    rec_dyn_template = 'B i'
    log_records = []
    with BytesIO(data) as log_stream:
        while True:
            fix_chunk = log_stream.read(rec_fix_size)
            if not fix_chunk:
                break
            fix_values = struct.unpack(rec_fix_format, fix_chunk)
            new_record = dict(record_template)
            for k, v in zip(missing_attrs, fix_values):
                conversion_fun = __value_conversion_lut[k]
                new_record[k] = conversion_fun(v)
            log_records.append(new_record)
            num_dlvs = fix_values[-1]
            if num_dlvs > 0:
                rec_dyn_format = '<' + (rec_dyn_template * num_dlvs)
                rex_dyn_size = struct.calcsize(rec_dyn_format)
                dyn_chunk = log_stream.read(rex_dyn_size)
                dyn_values = struct.unpack(rec_dyn_format, dyn_chunk)
                new_record['dlvs'] = list(zip(dyn_values[::2], dyn_values[1::2]))

    return log_records


def bin_log_to_dataframe(time_element: iso3.Time | iso4.Time, data: bytes) -> pd.DataFrame:
    data_log_value_types = [(DDEntity.from_bytes(dlv.process_data_ddi), dlv.device_element_id_ref)
                            for dlv in time_element.data_log_values]
    log_records = bin_log_to_dict(time_element, data)
    for log_record in log_records:
        for dlv in log_record['dlvs']:
            dd_entity, device_id = data_log_value_types[dlv[0]]
            value = dd_entity.bit_resolution * dlv[1]
            log_record[f'{device_id} ({dd_entity.name} [{dd_entity.unit}])'] = value
    df = pd.DataFrame.from_dict(log_records)
    df.drop(columns=['dlvs'], inplace=True)
    return df


if __name__ == '__main__':
    from isoxml.util.isoxml_io import isoxml_from_path
    from test.resources.test_resources import TEST_RES_DIR

    taskdata, external = isoxml_from_path(TEST_RES_DIR / 'isoxml/v4/logs/TASKDATA/TASKDATA.XML')
    df = bin_log_to_dataframe(*external['TLG00001'])
    df.to_csv('isoxml_log.csv', index=False)
    pass
