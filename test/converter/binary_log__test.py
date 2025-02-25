import json
from decimal import Decimal

from isoxml.converter.binary_log import bin_log_to_dict
from isoxml.util.isoxml_io import isoxml_from_path
from test.resources.test_resources import TEST_RES_DIR

LOG_TEST_RES_DIR = TEST_RES_DIR / 'isoxml' / 'v4' / 'logs'


def test__bin_log_to_dict__when_compared_to_preparsed_data__expect_same_result():
    taskdata, external = isoxml_from_path(LOG_TEST_RES_DIR / 'TASKDATA/TASKDATA.XML')
    with open(LOG_TEST_RES_DIR / 'parsed.json') as f:
        expected = json.load(f)
    expected_logs = expected['timeLogs']

    log_dict = bin_log_to_dict(*external['TLG00001'])
    assert len(log_dict) == len(expected_logs)
    sample_log = log_dict[6]
    expected_log = expected_logs[6]
    assert sample_log['position_north'] == Decimal(str(expected_log['position']['PositionNorth']))
    assert sample_log['position_east'] == Decimal(str(expected_log['position']['PositionEast']))
    assert sample_log['position_up'] == Decimal(str(expected_log['position']['PositionUp']))
    sample_dlvs = [v for _, v in sample_log['dlvs']]
    expected_dlvs = [v for _, v in expected_log['values'].items()]
    assert sample_dlvs == expected_dlvs
