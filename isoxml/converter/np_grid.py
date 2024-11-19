import numpy as np

import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4
from isoxml.models.ddi_entities import DDEntity


def from_numpy_array(arr: np.ndarray, grid: iso3.Grid | iso4.Grid) -> bytes:
    match grid.type:
        case iso3.GridType.GridType1 | iso4.GridType.GridType1:
            return from_numpy_array_to_type_1(arr, grid)
        case iso3.GridType.GridType2 | iso4.GridType.GridType2:
            return from_numpy_array_to_type_2(arr, grid)
        case _:
            raise NotImplementedError


def to_numpy_array(
        grid_bin: bytes,
        grid: iso3.Grid | iso4.Grid,
        ddi_list: list[DDEntity] | None = None,
        scale=True
) -> np.ndarray:
    """
    Takes a byte encoded ISOXML Grid and converts it back to a numpy array.
    :param grid_bin: the bytes to the ISOXML Grid 1 or 2
    :param grid: the ISOXML Grid element, aka the metadata from the XML file
    :param ddi_list: (optional and only for type 2) a list of DDEntities to performe scaling
    and for korrekt interpretation of multi-value grids.
    :param scale: (only for type 2, default True) whether to scale the values.
    :return: the numpy representation of the grid
    """
    grid_shape = __extract_grid_shape(grid)
    scale_factor = None
    match grid.type:
        case iso3.GridType.GridType1 | iso4.GridType.GridType1:
            return np.frombuffer(grid_bin, dtype=np.uint8).reshape(grid_shape)
        case iso3.GridType.GridType2 | iso4.GridType.GridType2:
            if ddi_list:
                grid_shape = grid_shape + (len(ddi_list),)
                scale_factor = [ddi.bit_resolution for ddi in ddi_list]
            np_arr = np.frombuffer(grid_bin, dtype=np.int32).reshape(grid_shape)
            if scale and scale_factor:
                np_arr = np_arr.astype(np.float32) * scale_factor
            return np_arr
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


def from_numpy_array_to_type_2(
        arr: np.ndarray,
        grid: iso3.Grid | iso4.Grid,
        ddi_list: list[DDEntity] | None = None,
        scale=True
) -> bytes:
    """
    converts a numpy array into isoxml binary grid type 2 format
    :param arr: the numpy array, dtype must be convertible to int32, dim order must be (row, column, pdv)
    :param grid: the isoxml grid element
    :param ddi_list: a list of DDEntities to performe scaling and for korrekt interpretation of multi-value girds.
    :param scale: whether to scale the values.
    :return: bytes of isoxml binary grid type 2 format
    """
    grid_shape = __extract_grid_shape(grid)
    if ddi_list and len(ddi_list) > 1:
        grid_shape = grid_shape + (len(ddi_list),)
    if arr.shape != grid_shape:
        raise ValueError("numpy shape dose not match grid shape")

    if scale and ddi_list:
        scale_factor = [int(1 / ddi.bit_resolution) for ddi in ddi_list]
        arr = np.round(arr * scale_factor, decimals=0)
        arr_int32 = arr.astype(dtype=np.int32, order='C', casting='unsafe', copy=True)
    else:
        try:
            arr_int32 = arr.astype(dtype=np.int32, order='C', casting='safe', copy=True)
        except (TypeError, ValueError) as e:
            raise ValueError("cant convert given arr to type int16", e)
    return arr_int32.tobytes(order='C')
