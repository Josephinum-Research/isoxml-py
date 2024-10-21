"""
if you already have a TASKDATA.XML file that works on your terminal (e.g. has been exported)
you can save yourself some work by simply generating the required Python code via xsdata.
The resulting code will be very detailed, but in most cases it is a good starting point.

see: https://xsdata.readthedocs.io/en/latest/data_binding/pycode_serializing/
"""

from xsdata.formats.dataclass.serializers import PycodeSerializer

from isoxml.util.isoxml_io import isoxml_from_path
from test.resources.test_resources import TEST_RES_DIR

task_data = isoxml_from_path(TEST_RES_DIR / 'isoxml/v4/cnh_export/TASKDATA.XML')

pycode_generator = PycodeSerializer()
with open('./output/generated_code.py', 'w', encoding='utf-8') as code_file:
    code_file.write(pycode_generator.render(task_data, var_name="task_data"))
