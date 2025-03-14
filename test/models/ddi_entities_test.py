import pytest

from isoxml.models.ddi_entities import DDEntity


def test__from_ddi__when_id_known__expect_ddi_entry():
    entry = DDEntity.from_id(1)
    assert isinstance(entry, DDEntity)


def test__from_ddi__when_id_unknown__expect_error():
    with pytest.raises(KeyError):
        DDEntity.from_id(9999999)


def test__to_bytes__when_dde_valid__expect_bytes():
    entry = DDEntity.from_id(60)
    assert bytes(entry) == b'\x00\x3c'


def test__from_bytes__when_byte_code_known__expect_entry():
    entry = DDEntity.from_bytes(b'\x00\x3c')
    assert entry.ddi == 60

def test__from_ddi__when_dict_has_missing_keys__expect_ddi_entry():
    entry = DDEntity.from_id(160)
    assert isinstance(entry, DDEntity)