import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4
from isoxml.util.external_file import merge_ext_content


def test__merge_ext_content__when_not_inplace__expect_unaltered_data():
    task_data = iso3.Iso11783TaskData(
        management_software_manufacturer="josephinum research",
        management_software_version="0.0.1",
        data_transfer_origin=iso3.Iso11783TaskDataDataTransferOrigin.FMIS
    )
    customer = iso3.Customer(id='CTR1234', designator='test_ctr')
    ext_ref = iso3.ExternalFileReference(filename='CTR1234', filetype=iso3.ExternalFileReferenceType.XML)
    ext_file = iso3.ExternalFileContents(customers=[customer])
    task_data.external_file_references = [ext_ref]
    ext_ref_dict = {'CTR1234': ext_file}
    merged_task_data, unmerged_refs = merge_ext_content(task_data, ext_ref_dict, inplace=False)
    assert customer in merged_task_data.customers
    assert customer not in task_data.customers
    assert unmerged_refs == {}
    assert 'CTR1234' in ext_ref_dict


def test__merge_ext_content__when_inplace__expect_altered_data():
    task_data = iso4.Iso11783TaskData(
        management_software_manufacturer="josephinum research",
        management_software_version="0.0.1",
        data_transfer_origin=iso4.Iso11783TaskDataDataTransferOrigin.FMIS
    )
    customer = iso4.Customer(id='CTR1234', last_name='test_ctr')
    ext_ref = iso4.ExternalFileReference(filename='CTR1234', filetype=iso4.ExternalFileReferenceType.XML)
    ext_file = iso4.ExternalFileContents(customers=[customer])
    task_data.external_file_references = [ext_ref]
    ext_ref_dict = {'CTR1234': ext_file}
    merge_ext_content(task_data, ext_ref_dict, inplace=True)
    assert customer in task_data.customers
    assert ext_ref_dict == {}


def test__merge_ext_content__when_unreferenced_obj_in_dict__expect_obj_remain_in_dict():
    task_data = iso3.Iso11783TaskData(
        management_software_manufacturer="josephinum research",
        management_software_version="0.0.1",
        data_transfer_origin=iso3.Iso11783TaskDataDataTransferOrigin.FMIS
    )
    customer = iso3.Customer(id='CTR1234', designator='test_ctr')
    ext_file = iso3.ExternalFileContents(customers=[customer])
    ext_ref_dict = {'CTR1234': ext_file}
    merge_ext_content(task_data, ext_ref_dict, inplace=True)
    assert 'CTR1234' in ext_ref_dict
