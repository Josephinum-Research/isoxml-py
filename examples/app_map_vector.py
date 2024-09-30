from pathlib import Path

import geopandas as gpd
import xmlschema

import isoxml.models.base.v4 as iso
from isoxml.converter.shapely_geom import ShapelyConverter
from isoxml.models.ddi_entities import DDEntities
from isoxml.util.isoxml_io import isoxml_to_dir
from resources.resources import RES_DIR

converter = ShapelyConverter('v4')

gdf_app_map = gpd.read_file("./input/app_map_vector.geojson")
gdf_app_map.to_crs('EPSG:4326', inplace=True)
gdf_border = gdf_app_map[gdf_app_map["name"] == "border"]
gdf_zones = gdf_app_map[gdf_app_map["dose"] >= 0]

assert gdf_border.shape[0] == 1

iso_border = converter.to_iso_polygon(shp_polygon=gdf_border.geometry.values[0],
                                      poly_type=iso.PolygonType.PartfieldBoundary)
partfield = iso.Partfield(
    polygons=[iso_border],
    id="PFD01",
    designator=gdf_border.name.values[0],
    area=int(gdf_border.to_crs(gdf_border.estimate_utm_crs()).area.values[0])
)

treatment_zones = []
tz_code = 0

for zone in gdf_zones.itertuples():
    pdv = iso.ProcessDataVariable(
        process_data_ddi=DDEntities['6']['DDI'].to_bytes(length=2, byteorder='big'),
        process_data_value=int(zone.dose)
    )

    poly = converter.to_iso_polygon(zone.geometry)

    treatment = iso.TreatmentZone(
        code=tz_code,
        designator=zone.name,
        process_data_variables=[pdv],
        polygons=[poly]
    )
    treatment_zones.append(treatment)
    tz_code += 1

task = iso.Task(
    id="TSK01",
    partfield_id_ref=partfield.id,
    status=iso.TaskStatus.Planned,
    treatment_zones=treatment_zones
)

task_data = iso.Iso11783TaskData(
    management_software_manufacturer="josephinum research",
    management_software_version="0.0.1",
    data_transfer_origin=iso.Iso11783TaskDataDataTransferOrigin.FMIS,
    partfields=[partfield],
    tasks=[task]
)

data_dir = Path('./output/app_map_vector')
data_dir.mkdir(parents=True, exist_ok=True)
isoxml_to_dir(data_dir, task_data)

xmlschema.validate(data_dir / 'TASKDATA.XML', RES_DIR / "xsd/ISO11783_TaskFile_V4-3.xsd")
