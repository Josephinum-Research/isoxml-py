"""
This example shows how to export a grid type 2.
With grid type 2, the applications values are written directly in the binary file. For this purpose,
the values are coded as an integer (int32).
The XML file only contains information on how these integer values must be scaled and shifted.
This grid type is particularly suitable for applications with many different values.

successful import/display on Deutz-Fahr 6140.4 + Bogballe L20W
successful import/display on New Holland T7 + IntelliView 12 + Kverneland iXter B18 (TC did not accept set-point)
"""
from decimal import Decimal

import numpy as np
import shapely as shp
from pathlib import Path


import isoxml.models.base.v3 as iso
from isoxml.converter.np_grid import from_numpy_array_to_type_2
from isoxml.converter.shapely_geom import ShapelyConverterV3
from isoxml.models.ddi_entities import DDEntity
from isoxml.util.isoxml_io import isoxml_to_zip

shp_converter = ShapelyConverterV3()
aoi = shp.from_wkt(
    "POLYGON ((15.1461618 48.1269217, 15.1461618 48.1267442, 15.1463363 48.1267442, 15.1463363 48.1269217, 15.1461618 48.1269217))")
iso_aoi = shp_converter.to_iso_polygon(aoi, iso.PolygonType.PartfieldBoundary)

customer = iso.Customer(id="CTR100", designator="jr_customer")
farm = iso.Farm(id="FRM100", designator="jr_farm", customer_id_ref=customer.id)
partfield = iso.Partfield(
    id="PFD100", designator="test_field", area=123456,
    customer_id_ref=customer.id, farm_id_ref=farm.id,
    polygons=[iso_aoi]
)

# keep in mind: ISOXML Grid coordinate system is bottom-up.
# therefore this image will appear upside down on your viewer/terminal
grid_data = np.array([
    [0, 1111],
    [2222, 3333]
])
y, x = grid_data.shape

dd_entity = DDEntity.from_id(6)

pdv_0 = iso.ProcessDataVariable(
    process_data_ddi=bytes(dd_entity),
    process_data_value=0
)

treatment_0 = iso.TreatmentZone(
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
    treatment_zone_code=treatment_0.code
)
grid_bin = from_numpy_array_to_type_2(grid_data, grid, ddi_list=[dd_entity])

task = iso.Task(
    id="TSK100",
    designator="task_grid_type_2",
    status=iso.TaskStatus.Initial,
    grids=[grid],
    treatment_zones=[treatment_0],
    customer_id_ref=customer.id,
    farm_id_ref=farm.id,
    partfield_id_ref=partfield.id,
    default_treatment_zone_code=treatment_0.code,
    position_lost_treatment_zone_code=treatment_0.code,
    out_of_field_treatment_zone_code=treatment_0.code
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

with open(Path('examples') / 'output' / 'example_grid_2.zip', 'wb') as zip_file:
    isoxml_to_zip(zip_file, task_data, {grid.filename: grid_bin})
