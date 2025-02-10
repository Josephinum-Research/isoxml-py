"""
if you want to make sure that your created TASKDATA is truly valid according to the XSD spec,
you can perform the following validation:
"""
from pathlib import Path


import xmlschema
from xmlschema import XMLSchemaValidationError

import isoxml.models.base.v4 as iso
from isoxml.util.isoxml_io import isoxml_to_text

task_data_valid = iso.Iso11783TaskData(
    management_software_manufacturer="josephinum research",
    management_software_version="0.0.1",
    data_transfer_origin=iso.Iso11783TaskDataDataTransferOrigin.FMIS
)

xml_content = isoxml_to_text(task_data_valid)
xmlschema.validate(xml_content, Path('resources') / "xsd/ISO11783_TaskFile_V4-3.xsd")

task_data_invalid = iso.Iso11783TaskData()

try:
    xmlschema.validate(isoxml_to_text(task_data_invalid), Path('resources') / "xsd/ISO11783_TaskFile_V4-3.xsd")
except XMLSchemaValidationError as e:
    print(e)
