from pathlib import Path

import shapely as shp

import isoxml.models.base.v4 as iso
from isoxml.converter.shapely_geom import ShapelyConverterV4
from isoxml.util.isoxml_io import isoxml_to_dir


shp_converter = ShapelyConverterV4()
swathe_width = 3000  # mm

ab_wkt = "LINESTRING (15.1472554 48.1263457, 15.1470881 48.1264582)"
ab_shp = shp.from_wkt(ab_wkt)
ab_iso = shp_converter.to_iso_line_string(ab_shp, iso.LineStringType.GuidancePattern)
ab_iso.points[0].type = iso.PointType.GuidanceReferenceA
ab_iso.points[1].type = iso.PointType.GuidanceReferenceB
ab_iso.width = swathe_width

curve_wkt = "LINESTRING (15.1452147 48.1259334, 15.1456092 48.1260317, 15.1459001 48.1260745, 15.1459019 48.1260748, 15.1459037 48.1260753, 15.1459053 48.1260758, 15.1464337 48.1262656, 15.1464345 48.1262658, 15.1468234 48.1264198, 15.1468253 48.1264207, 15.1468271 48.1264217, 15.1471490 48.1266280)"
curve_shp = shp.from_wkt(curve_wkt)
curve_iso = shp_converter.to_iso_line_string(curve_shp, iso.LineStringType.GuidancePattern)
for point in curve_iso.points:
    point.type = iso.PointType.GuidancePoint
curve_iso.points[0].type = iso.PointType.GuidanceReferenceA
curve_iso.points[-1].type = iso.PointType.GuidanceReferenceB
curve_iso.width = swathe_width

boundary_wkt = "POLYGON((15.1450455 48.1257726,15.1455444 48.1255685,15.1461560 48.1256759,15.1466280 48.1259194,15.1476044 48.1263777,15.1471484 48.1266463,15.1468131 48.1264314,15.1464242 48.1262775,15.1458958 48.1260877,15.1456034 48.1260447,15.1452011 48.1259445,15.1450455 48.1257726))"
boundary_shp = shp.from_wkt(boundary_wkt)
boundary_iso = shp_converter.to_iso_polygon(boundary_shp, iso.PolygonType.PartfieldBoundary)

customer = iso.Customer(id="CTR101", last_name="jr_customer")
farm = iso.Farm(id="FRM101", designator="jr_farm", customer_id_ref=customer.id)

ab_pattern = iso.GuidancePattern(
    id="GPN01",
    type=iso.GuidancePatternType.AB,
    designator="AB guidance pattern",
    line_strings=[ab_iso],
    propagation_direction=iso.GuidancePatternPropagationDirection.LeftDirectionOnly,
    extension=iso.GuidancePatternExtension.FromBothFirstAndLastPoint,
    number_of_swaths_left=10,
    number_of_swaths_right=0
)

curve_pattern = iso.GuidancePattern(
    id="GPN02",
    type=iso.GuidancePatternType.Curve,
    designator="curve guidance pattern",
    line_strings=[curve_iso],
    propagation_direction=iso.GuidancePatternPropagationDirection.RightDirectionOnly,
    extension=iso.GuidancePatternExtension.NoExtensions,
    number_of_swaths_left=0,
    number_of_swaths_right=4
)

guidance_group = iso.GuidanceGroup(
    id="GGP01",
    designator="test_guidance_group",
    guidance_patterns=[ab_pattern, curve_pattern]
)

partfield = iso.Partfield(
    id="PFD01",
    designator="test_partfield",
    area=1050,
    guidance_groups=[guidance_group],
    polygons=[boundary_iso],
    customer_id_ref=customer.id,
    farm_id_ref=farm.id
)

task_data = iso.Iso11783TaskData(
    management_software_manufacturer="josephinum research",
    management_software_version="0.0.1",
    data_transfer_origin=iso.Iso11783TaskDataDataTransferOrigin.FMIS,
    partfields=[partfield],
    customers=[customer],
    farms=[farm]
)

cwd = Path(__file__).parent


data_dir = cwd / 'output' / 'example_guidance'
data_dir.mkdir(parents=True, exist_ok=True)
isoxml_to_dir(data_dir, task_data)


try:
    import xmlschema

    path_resources = cwd.parent / 'resources'
    xmlschema.validate(data_dir / 'TASKDATA.XML', path_resources / "xsd/ISO11783_TaskFile_V4-3.xsd")
except ModuleNotFoundError:
    print('please install xmlschema, if you want to validate against the xsd schema')
