"""
This example shows how to create a vector based application map.
This type of map is useful if your application has not many different treatment zones.
This type of map could also be useful for spot sprayer applications (tests to follow).
The zones are modelled as TreatmentZones containing the dose and the geometry of the polygon.

successful import/display on New Holland T7 + IntelliView 12 + Kverneland iXter B18 (Terminal selection of DDI not possible)
"""

from pathlib import Path

import geopandas as gpd
import xmlschema

import isoxml.models.base.v4 as iso
from isoxml.converter.shapely_geom import ShapelyConverterV4
from isoxml.models.ddi_entities import DDEntity
from isoxml.util.isoxml_io import isoxml_to_dir
from resources.resources import RES_DIR

shp_converter = ShapelyConverterV4()
dd_entity = DDEntity.from_id(1)

gdf_app_map = gpd.read_file("./input/app_map_vector.geojson")
gdf_app_map.to_crs('EPSG:4326', inplace=True)
gdf_border = gdf_app_map[gdf_app_map["name"] == "border"]
gdf_zones = gdf_app_map[gdf_app_map["dose"] >= 0]

assert gdf_border.shape[0] == 1

iso_border = shp_converter.to_iso_polygon(shp_polygon=gdf_border.geometry.values[0],
                                          poly_type=iso.PolygonType.PartfieldBoundary)

customer = iso.Customer(id="CTR100", last_name="jr_customer")
farm = iso.Farm(id="FRM100", designator="jr_farm", customer_id_ref=customer.id)
partfield = iso.Partfield(
    polygons=[iso_border],
    id="PFD100",
    designator=gdf_border.name.values[0],
    area=int(gdf_border.to_crs(gdf_border.estimate_utm_crs()).area.values[0]),
    customer_id_ref=customer.id,
    farm_id_ref=farm.id
)

treatment_zones = []
default_treatment_zone = iso.TreatmentZone(
    code=0,
    designator='no_zone',
    process_data_variables=[
        iso.ProcessDataVariable(
                process_data_ddi=bytes(dd_entity),
                process_data_value=0
            )
    ]
)
treatment_zones.append(default_treatment_zone)
tz_code = 1

for zone in gdf_zones.itertuples():
    pdv = iso.ProcessDataVariable(
        process_data_ddi=bytes(dd_entity),
        process_data_value=int(zone.dose / dd_entity.bit_resolution)
    )

    poly = shp_converter.to_iso_polygon(zone.geometry, iso.PolygonType.TreatmentZone)

    treatment = iso.TreatmentZone(
        code=tz_code,
        designator=zone.name,
        process_data_variables=[pdv],
        polygons=[poly]
    )
    treatment_zones.append(treatment)
    tz_code += 1

task = iso.Task(
    id="TSK100",
    partfield_id_ref=partfield.id,
    status=iso.TaskStatus.Planned,
    treatment_zones=treatment_zones,
    designator="vector application map",
    default_treatment_zone_code=default_treatment_zone.code,
    position_lost_treatment_zone_code=default_treatment_zone.code,
    out_of_field_treatment_zone_code=default_treatment_zone.code
)

task_data = iso.Iso11783TaskData(
    management_software_manufacturer="josephinum research",
    management_software_version="0.0.1",
    data_transfer_origin=iso.Iso11783TaskDataDataTransferOrigin.FMIS,
    partfields=[partfield],
    tasks=[task],
    farms=[farm],
    customers=[customer]
)

data_dir = Path('./output/app_map_vector')
data_dir.mkdir(parents=True, exist_ok=True)
isoxml_to_dir(data_dir, task_data)

xmlschema.validate(data_dir / 'TASKDATA.XML', RES_DIR / "xsd/ISO11783_TaskFile_V4-3.xsd")
