from decimal import Decimal

import pytest
import shapely as shp

import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4
from isoxml.converter.shapely_geom import ShapelyConverterV3, ShapelyConverterV4
from isoxml.models.base.v4 import Point as Point_v4


@pytest.fixture
def converter_v3():
    return ShapelyConverterV3()


@pytest.fixture
def converter_v4():
    return ShapelyConverterV4()


def test_v3_to_iso_point(converter_v3):
    y, x = (Decimal('-89.9'), Decimal('179.55'))
    shp_point = shp.Point(x, y)
    iso_point = converter_v3.to_iso_point(shp_point)
    assert isinstance(iso_point, iso3.Point)
    assert iso_point.north == y
    assert iso_point.east == x


def test_v3_to_shapely_point(converter_v3):
    y, x = (Decimal(-89.9), Decimal(179.55))
    iso_point = iso3.Point(
        type=iso3.PointType.Other,
        north=y,
        east=x
    )
    shp_pnt = converter_v3.to_shapely_point(iso_point)
    assert isinstance(shp_pnt, shp.Point)
    assert shp_pnt.x == x
    assert shp_pnt.y == y


def test_v3_linestring(converter_v3):
    ls = shp.LineString([[0, 0], [1, 0], [1, 1]])
    iso_ls = converter_v3.to_iso_line_string(ls, iso3.LineStringType.Drainage)
    assert isinstance(iso_ls, iso3.LineString)
    test_pnt = iso_ls.points[1]
    assert test_pnt.north == 0
    assert test_pnt.east == 1
    shp_ls = converter_v3.to_shapely_line_string(iso_ls)
    assert shp_ls.equals(ls)


def test_v3_linestring_implicit_closing(converter_v3):
    iso_ls = iso3.LineString(points=[
        iso3.Point(type=iso3.PointType.Other, north=Decimal(0), east=Decimal(0)),
        iso3.Point(type=iso3.PointType.Other, north=Decimal(0), east=Decimal(1)),
        iso3.Point(type=iso3.PointType.Other, north=Decimal(1), east=Decimal(1))
    ], type=iso3.LineStringType.PolygonExterior)
    shp_ls = converter_v3.to_shapely_line_string(iso_ls)
    assert shp.is_closed(shp_ls)


def test_v3_polygon(converter_v3):
    poly = shp.Polygon(
        shell=[[10, 0], [0, 0], [0, 10], [10, 0]],
        holes=[
            [[1, 1], [2, 1], [2, 2], [1, 1]],
            [[4, 4], [3, 4], [3, 3], [4, 4]]
        ]
    )
    iso_poly = converter_v3.to_iso_polygon(poly)
    assert isinstance(iso_poly, iso3.Polygon)
    shp_poly = converter_v3.to_shapely_polygon(iso_poly)
    assert shp_poly.equals(poly)


def test_v3_multipoint(converter_v3):
    multipoint = shp.MultiPoint([[0.0, 0.0], [1.0, 2.0]])
    iso_points = converter_v3.to_iso_point_list(multipoint)
    assert isinstance(iso_points, list)
    assert isinstance(iso_points[0], iso3.Point)
    shp_multipoint = converter_v3.to_shapely_multi_point(iso_points)
    assert shp_multipoint.equals(multipoint)


def test_v3_multi_linestring(converter_v3):
    multi_linestring = shp.MultiLineString([[[0, 0], [1, 2]], [[4, 4], [5, 6]]])
    iso_linestring_s = converter_v3.to_iso_line_string_list(multi_linestring, iso3.LineStringType.SamplingRoute)
    assert isinstance(iso_linestring_s, list)
    assert isinstance(iso_linestring_s[0], iso3.LineString)
    shp_multi_linestring = converter_v3.to_shapely_multi_line_string(iso_linestring_s)
    assert shp_multi_linestring.equals(multi_linestring)


def test_v3_multi_polygon(converter_v3):
    multi_polygon = shp.MultiPolygon([
        (((0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)),
         [((0.1, 0.1), (0.1, 0.2), (0.2, 0.2), (0.2, 0.1))])
    ])
    iso_polygon_s = converter_v3.to_iso_polygon_list(multi_polygon)
    assert isinstance(iso_polygon_s, list)
    assert isinstance(iso_polygon_s[0], iso3.Polygon)
    shp_multi_polygon = converter_v3.to_shapely_multi_polygon(iso_polygon_s)
    assert shp_multi_polygon.equals(multi_polygon)


def test_v4_from_shapely_point(converter_v4):
    y, x = (-89.9, 179.55)
    shp_point = shp.Point(x, y)
    iso_point = converter_v4.to_iso_point(shp_point)
    assert isinstance(iso_point, Point_v4)


def test_v4_to_shapely_point(converter_v4):
    y, x = (Decimal(-89.9), Decimal(179.55))
    iso_point = iso4.Point(
        type=iso3.PointType.Other,
        north=y,
        east=x
    )
    shp_pnt = converter_v4.to_shapely_point(iso_point)
    assert isinstance(shp_pnt, shp.Point)


def test_v4_polygon(converter_v4):
    poly = shp.Polygon(
        shell=[[10, 0], [0, 0], [0, 10], [10, 0]],
        holes=[
            [[1, 1], [2, 1], [2, 2], [1, 1]],
            [[4, 4], [3, 4], [3, 3], [4, 4]]
        ]
    )
    iso_poly = converter_v4.to_iso_polygon(poly)
    assert isinstance(iso_poly, iso4.Polygon)
    shp_poly = converter_v4.to_shapely_polygon(iso_poly)
    assert shp_poly.equals(poly)


def test_v4_linestring_single_point(converter_v4):
    iso_ls = iso4.LineString(points=[
        iso4.Point(type=iso4.PointType.GuidanceReferenceA, north=Decimal(0), east=Decimal(0)),
    ])
    shp_ls = converter_v4.to_shapely_line_string(iso_ls)
    assert len(shp_ls.coords) == 2
    assert not shp.is_valid(shp_ls)


def test_v4_polygon_implicit_shell(converter_v4):
    # seen in test/resources/isoxml/v4/cnh_export/TASKDATA 1.XML
    iso_poly = iso4.Polygon(
        type=iso4.PolygonType.Flag,
        line_strings=[
            iso4.LineString(type=iso4.LineStringType.Flag, points=[
                iso4.Point(type=iso4.PointType.Flag, north=Decimal(0), east=Decimal(0)),
                iso4.Point(type=iso4.PointType.Flag, north=Decimal(0), east=Decimal(1)),
                iso4.Point(type=iso4.PointType.Flag, north=Decimal(1), east=Decimal(1)),
                iso4.Point(type=iso4.PointType.Flag, north=Decimal(0), east=Decimal(0)),
            ])
        ]
    )
    converter_v4.to_shapely_polygon(iso_poly)
