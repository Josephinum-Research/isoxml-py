from dataclasses import fields
from copy import deepcopy

from isoxml.models.base import v3 as iso3, v4 as iso4


def merge_ext_content(
        task_data: iso3.Iso11783TaskData | iso4.Iso11783TaskData,
        ext_content_obj: dict[str, iso3.ExternalFileContents | iso4.ExternalFileContents],
        inplace=False
) -> tuple[iso3.Iso11783TaskData | iso4.Iso11783TaskData, dict[str, object]]:
    _task_data = task_data
    _ext_content_obj = ext_content_obj
    if not inplace:
        _task_data = deepcopy(task_data)
        _ext_content_obj = ext_content_obj.copy()

    iso_element_lookup = {}
    for field_meta in fields(_task_data):
        if 'name' in field_meta.metadata:
            iso_element_lookup[field_meta.metadata['name']] = field_meta.name
    for ext_ref in _task_data.external_file_references:
        ref_obj = _ext_content_obj.pop(ext_ref.filename)
        for value in ref_obj.__dict__.values():
            if isinstance(value, list) and len(value) > 0:
                td_var_name = iso_element_lookup[value[0].Meta.name]
                if hasattr(_task_data, td_var_name):
                    getattr(_task_data, td_var_name).extend(value)
    _task_data.external_file_references = []
    return _task_data, _ext_content_obj
