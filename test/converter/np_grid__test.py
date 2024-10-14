from decimal import Decimal

import numpy as np
import pytest

from isoxml.converter.np_grid import from_numpy_array_to_type_1, to_numpy_array, from_numpy_array_to_type_2
from isoxml.models.base.v3 import Grid, GridType
from isoxml.models.ddi_entities import DDEntity


def test__from_numpy_array_to_type_1__when_wrong_type__expect_error():
    arr = np.array(
        [[-1, 2], [3, 4]],
        dtype=np.int8
    )
    grid = Grid(
        maximum_column=2,
        maximum_row=2,
        type=GridType.GridType1
    )
    with pytest.raises(ValueError):
        from_numpy_array_to_type_1(arr, grid)


def test__from_numpy_array_to_type_1__when_wrong_shape__expect_error():
    arr = np.array(
        [1, 2, 3],
        dtype=np.uint8
    )
    grid = Grid(
        maximum_column=3,
        maximum_row=1,
        type=GridType.GridType1
    )
    with pytest.raises(ValueError):
        from_numpy_array_to_type_1(arr, grid)


def test__from_numpy_array_to_type_1__when_valid_input__expect_correct_bytes():
    arr = np.array(
        [[1, 2], [254, 255]],
        dtype=np.uint8
    )
    grid = Grid(
        maximum_column=2,
        maximum_row=2,
        type=GridType.GridType1
    )
    expected_bin = b'\x01\x02\xFE\xFF'
    grid_bin = from_numpy_array_to_type_1(arr, grid)
    assert isinstance(grid_bin, bytes)
    assert grid_bin == expected_bin


def test__to_numpy_array__when_grid_type_1__expect_correct_array():
    grid_bin = b'\x01\x02\xFE\xFF\x03\x04'
    y, x = (3, 2)
    grid = Grid(
        minimum_north_position=Decimal('48.143304983'),
        minimum_east_position=Decimal('15.141245418'),
        cell_north_size=0.0001,
        cell_east_size=0.0001,
        maximum_column=x,
        maximum_row=y,
        filename="GRD00000",
        type=GridType.GridType1
    )
    arr_expected = np.array([
        [1, 2],
        [254, 255],
        [3, 4]
    ], dtype=np.uint8)
    arr_actual = to_numpy_array(grid_bin, grid)
    assert np.array_equal(arr_expected, arr_actual)


def test__from_numpy_array_to_type_2__when_valid_input__expect_correct_bytes():
    y, x = (3, 2)
    arr = np.array([
        [-2147483648, 1],
        [2, 3],
        [4, 2147483647],
    ], dtype=np.int32)
    grid = Grid(
        maximum_column=x,
        maximum_row=y,
        type=GridType.GridType2
    )
    expected_bin = (
            b'\x00\x00\x00\x80' + b'\x01\x00\x00\x00'
            + b'\x02\x00\x00\x00' + b'\x03\x00\x00\x00'
            + b'\x04\x00\x00\x00' + b'\xFF\xFF\xFF\x7F'
    )
    grid_bin = from_numpy_array_to_type_2(arr, grid)
    assert grid_bin == expected_bin


def test__from_numpy_array_to_type_2__when_multi_pdv__expect_correct_bytes():
    y, x = (2, 2)
    arr = np.array([
        [[0, 0], [1, -1]],
        [[2, -2], [3, -3]],
    ], dtype=np.int16)
    grid = Grid(
        maximum_column=x,
        maximum_row=y,
        type=GridType.GridType2
    )
    expected_bin = (
            b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00'
            + b'\x01\x00\x00\x00' + b'\xFF\xFF\xFF\xFF'

            + b'\x02\x00\x00\x00' + b'\xFE\xFF\xFF\xFF'
            + b'\x03\x00\x00\x00' + b'\xFD\xFF\xFF\xFF'
    )
    ddi6 = DDEntity.from_id(6)  # has scale of 1
    grid_bin = from_numpy_array_to_type_2(arr, grid, ddi_list=[ddi6, ddi6], scale=False)
    assert grid_bin == expected_bin


def test__from_numpy_array_to_type_2__when_ddi_scaling__expect_correct_bytes():
    y, x = (2, 2)
    arr = np.array([
        [[0., 0.], [1., -0.01]],
        [[2., -0.02], [3., -0.03]],
    ])
    grid = Grid(
        maximum_column=x,
        maximum_row=y,
        type=GridType.GridType2
    )
    expected_bin = (
            b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00'
            + b'\x01\x00\x00\x00' + b'\xFF\xFF\xFF\xFF'

            + b'\x02\x00\x00\x00' + b'\xFE\xFF\xFF\xFF'
            + b'\x03\x00\x00\x00' + b'\xFD\xFF\xFF\xFF'
    )
    ddi1 = DDEntity.from_id(1)  # has scale of 0.01
    ddi6 = DDEntity.from_id(6)  # has scale of 1
    grid_bin = from_numpy_array_to_type_2(arr, grid, ddi_list=[ddi6, ddi1])
    assert grid_bin == expected_bin


def test__to_numpy_array__when_grid_type_2_simple__expect_correct_array():
    y, x = (2, 2)
    grid_bin = (
            b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00'
            + b'\x01\x00\x00\x00' + b'\xFF\xFF\xFF\xFF'
    )
    grid = Grid(
        maximum_column=x,
        maximum_row=y,
        type=GridType.GridType2
    )
    arr_expected = np.array([
        [0, 0],
        [1, -1],
    ], dtype=np.int32)
    arr_actual = to_numpy_array(grid_bin, grid)
    assert np.array_equal(arr_expected, arr_actual)


def test__to_numpy_array__when_grid_type_2_multi_ddi__expect_correct_array():
    y, x, pdv = (2, 2, 2)
    grid_bin = (
            b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00'
            + b'\x01\x00\x00\x00' + b'\xFF\xFF\xFF\xFF'

            + b'\x02\x00\x00\x00' + b'\xFE\xFF\xFF\xFF'
            + b'\x03\x00\x00\x00' + b'\xFD\xFF\xFF\xFF'
    )
    grid = Grid(
        maximum_column=x,
        maximum_row=y,
        type=GridType.GridType2
    )
    arr_scale_expected = np.array([
        [[0., 0.], [1., -0.01]],
        [[2., -0.02], [3., -0.03]],
    ], dtype=np.float32)
    arr_no_scale_expected = np.array([
        [[0, 0], [1, -1]],
        [[2, -2], [3, -3]],
    ], dtype=np.int32)
    ddi1 = DDEntity.from_id(1)  # has scale of 1
    ddi6 = DDEntity.from_id(6)  # has scale of 1
    arr_scaled = to_numpy_array(grid_bin, grid, ddi_list=[ddi6, ddi1])
    assert np.allclose(arr_scale_expected, arr_scaled)
    arr_no_scale = to_numpy_array(grid_bin, grid, ddi_list=[ddi6, ddi1], scale=False)
    assert np.array_equal(arr_no_scale_expected, arr_no_scale)
