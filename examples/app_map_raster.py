from decimal import Decimal

import numpy as np

import isoxml.models.base.v4 as iso
from isoxml.converter.np_grid import from_numpy_array_to_type_2
from isoxml.models.ddi_entities import DDEntities
from isoxml.util.isoxml_io import isoxml_to_zip

y, x = (20, 40)

grid_data = np.linspace(1, 10_000, num=y*x, dtype=np.int32).reshape(y, x)

pdv_0 = iso.ProcessDataVariable(
    process_data_ddi=DDEntities['6']['DDI'].to_bytes(length=2),
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
grid_bin = from_numpy_array_to_type_2(grid_data, grid)

task = iso.Task(
    id="TSK-01",
    status=iso.TaskStatus.Planned,
    grids=[grid],
    treatment_zones=[treatment_0]
)

task_data = iso.Iso11783TaskData(
    management_software_manufacturer="josephinum research",
    management_software_version="0.0.1",
    data_transfer_origin=iso.Iso11783TaskDataDataTransferOrigin.FMIS,
    tasks=[task]
)

with open('./output/app_map.zip', 'wb') as zip_file:
    isoxml_to_zip(zip_file, task_data, {grid.filename: grid_bin})
