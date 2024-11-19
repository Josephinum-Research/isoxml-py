import os
import tempfile
from decimal import Decimal
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

import pytest
import xmlschema

import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4
from isoxml.models.ddi_entities import DDEntities
from isoxml.util.isoxml_io import isoxml_from_xml_file, isoxml_from_text, isoxml_from_zip, isoxml_to_dir, isoxml_to_zip, \
    isoxml_to_text
from resources.resources import RES_DIR
from test.resources.test_resources import TEST_RES_DIR


@pytest.fixture()
def task_with_grid():
    task_data = iso4.Iso11783TaskData(
        management_software_manufacturer="josephinum research",
        management_software_version="0.0.1",
        data_transfer_origin=iso4.Iso11783TaskDataDataTransferOrigin.FMIS
    )

    pdv_0 = iso4.ProcessDataVariable(
        process_data_ddi=DDEntities['6']['DDI'].to_bytes(length=2, byteorder='big'),
        process_data_value=0
    )

    treatment_0 = iso4.TreatmentZone(
        code=0,
        designator="zone_0",
        process_data_variables=[pdv_0]
    )

    grid = iso4.Grid(
        minimum_north_position=round(Decimal(48.143304983), 9),
        minimum_east_position=round(Decimal(15.141245418), 9),
        cell_north_size=0.0001,
        cell_east_size=0.0001,
        maximum_column=2,
        maximum_row=2,
        filename="GRD00000",
        type=iso4.GridType.GridType2,
        treatment_zone_code=treatment_0.code
    )
    grid_bin = (
            b'\x00\x00\x00\x80' + b'\x01\x00\x00\x00'
            + b'\x02\x00\x00\x00' + b'\x03\x00\x00\x00'
    )
    bin_dict = {
        'GRD00000': grid_bin
    }

    task = iso4.Task(
        id="TSK-01",
        status=iso4.TaskStatus.Planned,
        grids=[grid],
        treatment_zones=[treatment_0]
    )

    task_data.tasks = [task]
    return task_data, bin_dict


def test__isoxml_from_text__when_str_valid__expect_pares_isoxml():
    xml_content = """<?xml version="1.0" encoding="UTF-8"?><ISO11783_TaskData VersionMajor="4" VersionMinor="3" ManagementSoftwareManufacturer="josephinum research" ManagementSoftwareVersion="0.0.1" DataTransferOrigin="1"></ISO11783_TaskData>"""
    task_data = isoxml_from_text(xml_content)
    assert isinstance(task_data, iso4.Iso11783TaskData)


def test__isoxml_from_xml_file__when_file_valid__expect_pares_isoxml():
    path = TEST_RES_DIR / 'isoxml/v3/grid_type_2/TASKDATA.XML'
    task_data, bin_dict = isoxml_from_xml_file(path)
    assert isinstance(task_data, iso3.Iso11783TaskData)
    assert 'GRD00001' in bin_dict


def test__isoxml_from_zip__when_file_valid__expect_pares_isoxml():
    path = TEST_RES_DIR / 'isoxml/v3/grid_type_2/grid_type_2.zip'
    task_data, bin_dict = isoxml_from_zip(path)
    assert isinstance(task_data, iso3.Iso11783TaskData)
    assert 'GRD00001' in bin_dict


def test__isoxml_to_text__when_file_valid__expect_valid_files(task_with_grid):
    task_data, _ = task_with_grid
    xml_content = isoxml_to_text(task_data)
    xmlschema.validate(xml_content, RES_DIR / "xsd/ISO11783_TaskFile_V4-3.xsd")


def test__isoxml_to_dir__when_file_valid__expect_valid_files(task_with_grid):
    task_data, bin_dict = task_with_grid

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        isoxml_to_dir(tmp_path, task_data, bin_dict)
        assert os.path.isfile(tmp_path / 'TASKDATA.XML')
        assert os.path.isfile(tmp_path / 'GRD00000.bin')


def test__isoxml_to_zip__when_write_to_buffer__expect_valid_files(task_with_grid):
    task_data, bin_dict = task_with_grid

    with BytesIO() as buffer:
        isoxml_to_zip(buffer, task_data, bin_dict)
        with ZipFile(buffer, 'r') as zip_archive:
            assert 'TASKDATA.XML' in zip_archive.namelist()
            assert 'GRD00000.bin' in zip_archive.namelist()


def test__isoxml_to_zip__when_write_to_file__expect_valid_files(task_with_grid):
    task_data, bin_dict = task_with_grid

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        zip_path = tmp_path / 'TASKDATA.zip'
        with open(zip_path, 'wb') as zip_file:
            isoxml_to_zip(zip_file, task_data, bin_dict)
        with ZipFile(zip_path, 'r') as zip_archive:
            assert 'TASKDATA.XML' in zip_archive.namelist()
            assert 'GRD00000.bin' in zip_archive.namelist()
