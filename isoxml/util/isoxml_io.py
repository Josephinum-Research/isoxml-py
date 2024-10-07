from pathlib import Path
from zipfile import ZipFile

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4

__parser = XmlParser()
__serializer = XmlSerializer(
    config=SerializerConfig(
        xml_version='1.0',
        encoding='UTF-8',
        indent='    '
    )
)


def isoxml_from_xml_file(xml_path: Path) -> tuple[iso3.Iso11783TaskData | iso4.Iso11783TaskData, dict[str, bytes]]:
    with open(xml_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    task_data = isoxml_from_text(xml_content)
    bin_dict = {}
    for task in task_data.tasks:
        for grid in task.grids:
            with open(xml_path.parent / (grid.filename + '.bin'), 'rb') as bin_file:
                bin_dict[grid.filename] = bin_file.read()
    return task_data, bin_dict


def isoxml_from_zip(zip_path: Path) -> tuple[iso3.Iso11783TaskData | iso4.Iso11783TaskData, dict[str, bytes]]:
    with ZipFile(zip_path, 'r') as zip_archive:
        with zip_archive.open('TASKDATA.XML', 'r') as xml_file:
            xml_content = xml_file.read().decode(encoding='utf-8')
        task_data = isoxml_from_text(xml_content)
        bin_dict = {}
        for task in task_data.tasks:
            for grid in task.grids:
                with zip_archive.open(grid.filename + '.bin', 'r') as bin_file:
                    bin_dict[grid.filename] = bin_file.read()
    return task_data, bin_dict


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
        dir_path: Path, task_data: iso3.Iso11783TaskData | iso4.Iso11783TaskData,
        bin_dict: dict[str, bytes] | None = None
) -> None:
    if not bin_dict:
        bin_dict = {}
    xml_path = dir_path / 'TASKDATA.XML'
    with open(xml_path, 'w', encoding='utf-8') as xml_file:
        __serializer.write(xml_file, task_data)
    for bin_name, bin_data in bin_dict.items():
        bin_path = dir_path / (bin_name + '.bin')
        with open(bin_path, 'wb') as bin_file:
            bin_file.write(bin_data)


def isoxml_to_zip(
        target,
        task_data: iso3.Iso11783TaskData | iso4.Iso11783TaskData,
        bin_dict: dict[str, bytes] | None = None,
        include_folder=True
) -> None:
    if not bin_dict:
        bin_dict = {}
    path_in_arch = 'TASKDATA/' if include_folder else ''
    with ZipFile(target, 'w') as zip_archive:
        with zip_archive.open(path_in_arch + 'TASKDATA.XML', 'w') as xml_file:
            xml_content = isoxml_to_text(task_data)
            xml_file.write(xml_content.encode('utf-8'))
        for bin_name, bin_data in bin_dict.items():
            bin_filename = bin_name + '.bin'
            with zip_archive.open(path_in_arch + bin_filename, 'w') as bin_file:
                bin_file.write(bin_data)
