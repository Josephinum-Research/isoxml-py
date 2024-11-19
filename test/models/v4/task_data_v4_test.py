from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from isoxml.models.base.v4 import Iso11783TaskData
from test.resources.test_resources import TEST_RES_DIR

parser = XmlParser()
serializer = XmlSerializer()


def test_parsing():
    task_data = parser.parse(TEST_RES_DIR / "isoxml" / "v4" / "full_task" /"TASKDATA.XML", Iso11783TaskData)
    assert isinstance(task_data, Iso11783TaskData)
