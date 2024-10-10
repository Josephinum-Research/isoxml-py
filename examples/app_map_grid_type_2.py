"""
This example shows how to export a grid type 2.
With grid type 2, the applications values are written directly in the binary file. For this purpose,
the values are coded as an integer (int32).
The XML file only contains information on how these integer values must be scaled and shifted.
This grid type is particularly suitable for applications with many different values.
"""
from decimal import Decimal

import numpy as np
import shapely as shp

import isoxml.models.base.v3 as iso
from isoxml.converter.np_grid import from_numpy_array_to_type_2
from isoxml.converter.shapely_geom import ShapelyConverter
from isoxml.models.ddi_entities import DDEntities
from isoxml.util.isoxml_io import isoxml_to_zip

shapely_converter = ShapelyConverter('v3')
aoi = shp.from_wkt("POLYGON ((15.1461618 48.1269217, 15.1461618 48.1267442, 15.1463363 48.1267442, 15.1463363 48.1269217, 15.1461618 48.1269217))")
iso_aoi = shapely_converter.to_iso_polygon(aoi, iso.PolygonType.PartfieldBoundary)

customer = iso.Customer(id="CTR100", designator="jr_customer")
farm = iso.Farm(id="FRM100", designator="jr_farm", customer_id_ref=customer.id)
partfield = iso.Partfield(
    id="PFD01", designator="test_field", area=123456,
    customer_id_ref=customer.id, farm_id_ref=farm.id,
    polygons=[iso_aoi]
)

grid_data = np.array([
    [267805, 1000],
    [3000, 2000]
], dtype=np.int32)
y, x = grid_data.shape

pdv_0 = iso.ProcessDataVariable(
    process_data_ddi=DDEntities['1']['DDI'].to_bytes(length=2, byteorder='big'),
    process_data_value=0
)

treatment = iso.TreatmentZone(
    code=0,
    designator="zone_0",
    process_data_variables=[pdv_0]
)

grid = iso.Grid(
    minimum_north_position=Decimal('48.12674'),
    minimum_east_position=Decimal('15.14615'),
    cell_north_size=0.0001,
    cell_east_size=0.0001,
    maximum_column=x,
    maximum_row=y,
    filename="GRD00000",
    type=iso.GridType.GridType2,
    treatment_zone_code=treatment.code
)
grid_bin = from_numpy_array_to_type_2(grid_data, grid)

task = iso.Task(
    id="TSK-01",
    designator="task_grid_type_2",
    status=iso.TaskStatus.Initial,
    grids=[grid],
    treatment_zones=[treatment],
    customer_id_ref=customer.id,
    farm_id_ref=farm.id,
    partfield_id_ref=partfield.id
)

task_data = iso.Iso11783TaskData(
    management_software_manufacturer="josephinum research",
    management_software_version="0.0.1",
    data_transfer_origin=iso.Iso11783TaskDataDataTransferOrigin.FMIS,
    tasks=[task],
    customers=[customer],
    farms=[farm],
    partfields=[partfield]
)

with open('./output/example_grid_2.zip', 'wb') as zip_file:
    isoxml_to_zip(zip_file, task_data, {grid.filename: grid_bin})
