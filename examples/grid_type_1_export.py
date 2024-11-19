"""
This example shows how to export a grid type 1.
the grid type 1 functions as a lookup table. the actual values are stored in xml.
this grid type is particularly interesting if only a few different values need to be stored in the application map.
If there are many different values, type 2 is preferable, otherwise the XML file becomes very large.
"""
from decimal import Decimal

import numpy as np

import isoxml.models.base.v3 as iso
from isoxml.converter.np_grid import from_numpy_array_to_type_1
from isoxml.models.ddi_entities import DDEntities
from isoxml.util.isoxml_io import isoxml_to_zip
from dataclasses import replace

y, x = (2, 2)

customer = iso.Customer(id="CTR01", designator="test_user")
farm = iso.Farm(id="FRM01", designator="test_farm", customer_id_ref=customer.id)
partfield = iso.Partfield(
    id="PFD01", designator="test_field", area=123456,
    customer_id_ref=customer.id, farm_id_ref=farm.id
)

grid_data = np.arange(y * x, dtype=np.uint8).reshape(y, x)

grid = iso.Grid(
    minimum_north_position=Decimal('48.12674'),
    minimum_east_position=Decimal('15.14615'),
    cell_north_size=0.0001,
    cell_east_size=0.0001,
    maximum_column=x,
    maximum_row=y,
    filename="GRD00000",
    type=iso.GridType.GridType1
)
grid_bin = from_numpy_array_to_type_1(grid_data, grid)

pdv_0 = iso.ProcessDataVariable(
    process_data_ddi=DDEntities['6']['DDI'].to_bytes(length=2),
    process_data_value=1
)
pdv_1 = replace(pdv_0, process_data_value=10)
pdv_2 = replace(pdv_0, process_data_value=20)
pdv_3 = replace(pdv_0, process_data_value=30)

treatment_0 = iso.TreatmentZone(
    code=0,
    designator="zone_0",
    process_data_variables=[pdv_0]
)
treatment_1 = iso.TreatmentZone(code=1, designator="zone_1", process_data_variables=[pdv_1])
treatment_2 = iso.TreatmentZone(code=2, designator="zone_2", process_data_variables=[pdv_2])
treatment_3 = iso.TreatmentZone(code=3, designator="zone_3", process_data_variables=[pdv_3])

task = iso.Task(
    id="TSK-01",
    designator="task_grid_type_1",
    status=iso.TaskStatus.Initial,
    grids=[grid],
    treatment_zones=[treatment_0, treatment_1, treatment_2, treatment_3],
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

with open('./output/example_grid_1.zip', 'wb') as zip_file:
    isoxml_to_zip(zip_file, task_data, {grid.filename: grid_bin})
