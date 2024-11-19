import os.path
import tempfile
from pathlib import Path
from types import ModuleType
from typing import Literal
from zipfile import ZipFile

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4
from isoxml.util.external_file import merge_ext_content

__parser = XmlParser(ParserConfig(
    fail_on_unknown_properties=False,
    fail_on_unknown_attributes=False
))
__serializer = XmlSerializer(
    config=SerializerConfig(
        xml_version='1.0',
        encoding='UTF-8',
        indent='    '
    )
)


def __select_base_module(xml_content: str) -> ModuleType:
    xml_head = xml_content[:1024]
    if 'VersionMajor="4"' in xml_head:
        return iso4
    elif 'VersionMajor="3"' in xml_head:
        return iso3
    else:
        raise ValueError("the provided xml file is neither version 3 or 4")


def isoxml_from_path(
        task_data_path: Path,
        external_files: Literal['merge', 'ignore', 'separate'] = 'merge',
        read_bin_files=True
) -> tuple[
    iso3.Iso11783TaskData | iso4.Iso11783TaskData,
    dict[str, bytes | iso3.ExternalFileContents | iso4.ExternalFileContents]
]:
    if task_data_path.is_file():
        task_data_path = task_data_path.parent

    with open(task_data_path / 'TASKDATA.XML', 'r', encoding='utf-8') as file:
        xml_content = file.read()
    iso = __select_base_module(xml_content)
    task_data: iso4.Iso11783TaskData | iso3.Iso11783TaskData = __parser.from_string(xml_content, iso.Iso11783TaskData)

    ext_file_obj_dict = {}
    file_in_dir = os.listdir(task_data_path)
    if external_files in ('merge', 'separate'):
        for ext_ref in task_data.external_file_references:
            assert ext_ref.filetype == iso.ExternalFileReferenceType.XML
            fitting_files = [file_name for file_name in file_in_dir if file_name.startswith(ext_ref.filename)]
            assert len(fitting_files) == 1
            full_ref_filename = fitting_files[0]
            ext_file_obj_dict[ext_ref.filename] = __parser.from_path(
                task_data_path / full_ref_filename,
                iso.ExternalFileContents
            )
    if external_files == 'merge':
        merge_ext_content(task_data, ext_file_obj_dict, inplace=True)

    bin_dict = {}
    if read_bin_files:
        for file_name in file_in_dir:
            if file_name.lower().endswith('.bin') and file_name.startswith(('GRD', 'TLG', 'PNT')):
                iso_id_ref = file_name.rsplit('.')[0]
                with open(task_data_path / file_name, 'rb') as bin_files:
                    bin_dict[iso_id_ref] = bin_files.read()

    return task_data, bin_dict | ext_file_obj_dict


def isoxml_from_zip(
        zip_path: Path,
        external_files: Literal['merge', 'ignore', 'separate'] = 'merge',
        read_bin_files=True
) -> tuple[
    iso3.Iso11783TaskData | iso4.Iso11783TaskData,
    dict[str, bytes | iso3.ExternalFileContents | iso4.ExternalFileContents]
]:
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        with ZipFile(zip_path, 'r') as zip_archive:
            zip_archive.extractall(tmp_path)
        return isoxml_from_path(tmp_path, external_files, read_bin_files)


def isoxml_from_text(xml_content: str) -> iso3.Iso11783TaskData | iso4.Iso11783TaskData:
    if 'VersionMajor="4"' in xml_content:
        iso = iso4
    elif 'VersionMajor="3"' in xml_content:
        iso = iso3
    else:
        raise ValueError("the provided xml file is neither version 3 or 4")
    return __parser.from_string(xml_content, iso.Iso11783TaskData)


def isoxml_to_text(task_data: iso3.Iso11783TaskData | iso4.Iso11783TaskData) -> str:
    return __serializer.render(task_data)


def isoxml_to_dir(
        dir_path: Path,
        task_data: iso3.Iso11783TaskData | iso4.Iso11783TaskData,
        ext_refs: dict[str, bytes | iso3.ExternalFileContents | iso4.ExternalFileContents] | None = None
) -> None:
    if not ext_refs:
        ext_refs = {}
    xml_path = dir_path / 'TASKDATA.XML'
    with open(xml_path, 'w', encoding='utf-8') as xml_file:
        __serializer.write(xml_file, task_data)
    for ref_name, ref_data in ext_refs.items():
        if isinstance(ref_data, bytes):
            bin_path = dir_path / (ref_name + '.bin')
            with open(bin_path, 'wb') as bin_file:
                bin_file.write(ref_data)
        elif isinstance(ref_data, (iso3.ExternalFileContents, iso4.ExternalFileContents)):
            xml_path = dir_path / (ref_name + '.XML')
            with open(xml_path, 'w', encoding='utf-8') as xml_file:
                __serializer.write(xml_file, ref_data)
        else:
            raise ValueError(f'unknown type {type(ref_data)} of external ref {ref_name}')


def isoxml_to_zip(
        target,
        task_data: iso3.Iso11783TaskData | iso4.Iso11783TaskData,
        ext_refs: dict[str, bytes | iso3.ExternalFileContents | iso4.ExternalFileContents] | None = None,
        include_folder=True
) -> None:
    if not ext_refs:
        ext_refs = {}
    path_in_arch = 'TASKDATA/' if include_folder else ''
    with ZipFile(target, 'w') as zip_archive:
        with zip_archive.open(path_in_arch + 'TASKDATA.XML', 'w') as xml_file:
            xml_content = isoxml_to_text(task_data)
            xml_file.write(xml_content.encode('utf-8'))

        for ref_name, ref_data in ext_refs.items():
            if isinstance(ref_data, bytes):
                bin_filename = path_in_arch + ref_name + '.bin'
                with zip_archive.open(bin_filename, 'w') as bin_file:
                    bin_file.write(ref_data)
            elif isinstance(ref_data, (iso3.ExternalFileContents, iso4.ExternalFileContents)):
                xml_filename = path_in_arch + ref_name + '.XML'
                with zip_archive.open(xml_filename, 'w') as xml_file:
                    xml_content = __serializer.render(ref_data)
                    xml_file.write(xml_content.encode('utf-8'))
            else:
                raise ValueError(f'unknown type {type(ref_data)} of external ref {ref_name}')
