import shapely as shp
from pathlib import Path


from isoxml.converter.shapely_geom import ShapelyConverterV4
import isoxml.models.base.v4 as iso
from isoxml.util.isoxml_io import isoxml_to_zip

aoi = shp.from_wkt(
    "POLYGON((15.1447424 48.1255056, 15.1474165 48.1261199, 15.1473747 48.1262158, 15.1482940 48.1263951, 15.1483067 48.1264138, 15.1482915 48.1264792, 15.1482606 48.1265468, 15.1482752 48.1265771, 15.1482575 48.1266392, 15.1481435 48.1267167, 15.1479174 48.1268654, 15.1476676 48.1270070, 15.1475497 48.1270453, 15.1473535 48.1271016, 15.1470970 48.1271263, 15.1461062 48.1271846, 15.1451041 48.1274747, 15.1445809 48.1272868, 15.1441020 48.1270989, 15.1446598 48.1260670, 15.1447174 48.1259533, 15.1447382 48.1258014, 15.1447195 48.1257321, 15.1447079 48.1255547, 15.1447418 48.1255612, 15.1447424 48.1255056))"
)

converter = ShapelyConverterV4()
iso_poly = converter.to_iso_polygon(shp_polygon=aoi, poly_type=iso.PolygonType.PartfieldBoundary)
partfield = iso.Partfield(
    polygons=[iso_poly],
    id="PFD01",
    designator="test_partfield",
    area=39800
)

task = iso.Task(
    id="TSK01",
    partfield_id_ref=partfield.id,
    status=iso.TaskStatus.Running
)

task_data = iso.Iso11783TaskData(
    management_software_manufacturer="josephinum research",
    management_software_version="0.0.1",
    data_transfer_origin=iso.Iso11783TaskDataDataTransferOrigin.FMIS,
    partfields=[partfield],
    tasks=[task]
)

base_dir = Path(__file__).parent
output_path = base_dir / 'output' / 'example_partfield.zip'


with open(output_path, 'wb') as zip_file:
    isoxml_to_zip(zip_file, task_data)
