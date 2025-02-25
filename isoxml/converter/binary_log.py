import struct
from dataclasses import dataclass, asdict
from datetime import time, date
from decimal import Decimal
from io import BytesIO

from dateutil import tz

import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4


@dataclass
class _Record:
    time_of_day: time
    date: date
    position_north: Decimal
    position_east: Decimal
    position_up: int
    position_status: bytes
    pdop: Decimal
    hdop: Decimal
    number_of_satellites: bytes
    gps_utc_time: time
    gps_utc_date: date
    dlvs: list[tuple[bytes, int]]


empty_record = {
    'time_of_day': None,
    'date': None,
    'position_north': None,
    'position_east': None,
    'position_up': None,
    'position_status': None,
    'pdop': None,
    'hdop': None,
    'number_of_satellites': None,
    'gps_utc_time': None,
    'gps_utc_date': None,
    'dlvs': None,
}

lookup_dict = {
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

UTC = tz.gettz('UTC')


def to_time(ms_sinc_midnight: int, tzinfo=None) -> time:
    hours = ms_sinc_midnight // (1000 * 60 * 60)
    minutes = (ms_sinc_midnight % (1000 * 60 * 60)) // (1000 * 60)
    seconds = (ms_sinc_midnight % (1000 * 60)) // 1000
    microseconds = ms_sinc_midnight % 1000

    return time(hour=hours, minute=minutes, second=seconds, microsecond=microseconds, tzinfo=None)


conversion = {
    'time_of_day': to_time,
    'date': lambda x: date.fromtimestamp(x * 24 * 60 * 60),
    'position_north': lambda x: Decimal(x) * Decimal('1e-7'),
    'position_east': lambda x: Decimal(x) * Decimal('1e-7'),
    'position_up': lambda x: x,
    'position_status': lambda x: x,
    'pdop': lambda x: Decimal(x) * Decimal('1e-1'),
    'hdop': lambda x: Decimal(x) * Decimal('1e-1'),
    'number_of_satellites': lambda x: x,
    'gps_utc_time': lambda x: to_time(x, UTC),
    'gps_utc_date': lambda x: date.fromtimestamp(x * 24 * 60 * 60),
}


def bin_log_to_dict(time_element: iso3.Time | iso4.Time, data: bytes) -> list:
    assert len(time_element.positions) == 1, "this not not forbidden, but i don't understand it"
    position_header = time_element.positions[0]
    record_template = _Record(
        time_of_day=None,
        date=None,
        position_north=position_header.north,
        position_east=position_header.east,
        position_up=position_header.up,
        position_status=position_header.status,
        pdop=position_header.pdop,
        hdop=position_header.hdop,
        number_of_satellites=position_header.number_of_satellites,
        gps_utc_time=position_header.gps_utc_time,
        gps_utc_date=position_header.gps_utc_date,
        dlvs=[]
    )

    rec_fix_format = '<'
    missing_attrs = []
    for k, v in asdict(record_template).items():
        if (not v or v == '') and k in lookup_dict:
            rec_fix_format += lookup_dict[k]
            missing_attrs.append(k)
    rec_fix_format += 'B'
    rec_fix_size = struct.calcsize(rec_fix_format)
    rec_dyn_template = 'B i'
    records = []
    with BytesIO(data) as log_stream:
        while True:
            fix_chunk = log_stream.read(rec_fix_size)
            if not fix_chunk:
                break
            fix_values = struct.unpack(rec_fix_format, fix_chunk)
            new_record = asdict(record_template)
            for k, v in zip(missing_attrs, fix_values):
                func = conversion[k]
                new_record[k] = func(v)
            records.append(new_record)
            num_dlvs = fix_values[-1]
            if num_dlvs > 0:
                rec_dyn_format = '<' + (rec_dyn_template * num_dlvs)
                rex_dyn_size = struct.calcsize(rec_dyn_format)
                dyn_chunk = log_stream.read(rex_dyn_size)
                dyn_values = struct.unpack(rec_dyn_format, dyn_chunk)
                new_record['dlvs'] = list(zip(dyn_values[::2], dyn_values[1::2]))

    return records


if __name__ == '__main__':
    from isoxml.util.isoxml_io import isoxml_from_path
    from test.resources.test_resources import TEST_RES_DIR

    taskdata, external = isoxml_from_path(TEST_RES_DIR / 'isoxml/v4/logs/TASKDATA/TASKDATA.XML')
    records = bin_log_to_dict(*external['TLG00001'])
    import pandas as pd
    df = pd.DataFrame.from_dict(records)
