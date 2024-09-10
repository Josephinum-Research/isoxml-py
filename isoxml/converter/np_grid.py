import numpy as np

import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4


def from_numpy_array(arr: np.ndarray, grid: iso3.Grid | iso4.Grid) -> bytes:
    match grid.type:
        case iso3.GridType.GridType1 | iso4.GridType.GridType1:
            return from_numpy_array_to_type_1(arr, grid)
        case iso3.GridType.GridType2 | iso4.GridType.GridType2:
            return from_numpy_array_to_type_2(arr, grid)
        case _:
            raise NotImplementedError


def to_numpy_array(grid_bin: bytes, grid: iso3.Grid | iso4.Grid, number_pdv: None | int = None) -> np.ndarray:
    grid_shape = __extract_grid_shape(grid)
    match grid.type:
        case iso3.GridType.GridType1 | iso4.GridType.GridType1:
            return np.frombuffer(grid_bin, dtype=np.uint8).reshape(grid_shape)
        case iso3.GridType.GridType2 | iso4.GridType.GridType2:
            if number_pdv:
                grid_shape = grid_shape + (number_pdv,)
            return np.frombuffer(grid_bin, dtype=np.int32).reshape(grid_shape)
        case _:
            raise NotImplementedError


def __extract_grid_shape(grid):
    grid_shape = (grid.maximum_row, grid.maximum_column)
    return grid_shape


def from_numpy_array_to_type_1(arr: np.ndarray, grid: iso3.Grid | iso4.Grid) -> bytes:
    if arr.dtype != np.uint8:
        raise ValueError("grid type 1 requires uint8")
    grid_shape = __extract_grid_shape(grid)
    if arr.shape != grid_shape:
        raise ValueError("numpy shape dose not match grid shape")
    return arr.tobytes(order="C")


def from_numpy_array_to_type_2(arr: np.ndarray, grid: iso3.Grid | iso4.Grid, number_pdv: None | int = None) -> bytes:
    """
    converts a numpy array into isoxml binary grid type 2 format
    :param arr: the numpy array, dtype must be convertible to int32, dim order must be (row, column, pdv)
    :param grid: the isoxml grid element
    :param number_pdv: the number of ProcessDataVariable that should be encoded
    :return: bytes of isoxml binary grid type 2 format
    """
    grid_shape = __extract_grid_shape(grid)
    if number_pdv:
        grid_shape = grid_shape + (number_pdv,)

    if arr.shape != grid_shape:
        raise ValueError("numpy shape dose not match grid shape")
    try:
        arr_int32 = arr.astype(dtype=np.int32, order='C', casting='safe', copy=True).reshape(grid_shape)
    except (TypeError, ValueError) as e:
        raise ValueError("cant convert given arr to type int16", e)
    return arr_int32.tobytes(order='C')
