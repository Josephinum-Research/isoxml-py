from io import BytesIO

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from isoxml.models.base.v3 import (
    Iso11783TaskData, Iso11783TaskDataDataTransferOrigin, Farm
)
from tests.resources.test_resources import TEST_RES_DIR

parser = XmlParser()
serializer = XmlSerializer()


def test_roundtrip():
    task_data = Iso11783TaskData(
        management_software_manufacturer="josephinum research",
        management_software_version="0.0.1",
        data_transfer_origin=Iso11783TaskDataDataTransferOrigin.FMIS
    )

    farm = Farm(
        id="FRM01",
        designator="jr_test_farm_1"
    )

    task_data.farms = [farm]

    xml_content = serializer.render(task_data)
    with BytesIO(xml_content.encode('utf-8')) as rendered_xml_file:
        task_data_2 = parser.parse(rendered_xml_file, Iso11783TaskData)
    assert task_data_2 == task_data


def test_parsing():
    task_data = parser.parse(TEST_RES_DIR / "isoxml" / "v3" / "grid_type_2" / "TASKDATA.XML", Iso11783TaskData)
    assert isinstance(task_data, Iso11783TaskData)
    assert task_data.tasks[0].designator == "BH-Feld"


def test_parsing_empty():
    task_data = parser.parse(TEST_RES_DIR / "isoxml" / "v3" / "empty" / "TASKDATA.XML", Iso11783TaskData)
    assert isinstance(task_data, Iso11783TaskData)
