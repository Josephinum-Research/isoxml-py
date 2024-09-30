from decimal import Decimal

import pytest
import shapely as shp

import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4
from isoxml.converter.shapely_geom import ShapelyConverter
from isoxml.models.base.v4 import Point as Point_v4


@pytest.fixture
def converter():
    return ShapelyConverter(version='v3')


@pytest.fixture
def converter_v4():
    return ShapelyConverter(version='v4')


def test_to_iso_point(converter):
    y, x = (Decimal('-89.9'), Decimal('179.55'))
    shp_point = shp.Point(x, y)
    iso_point = converter.to_iso_point(shp_point)
    assert isinstance(iso_point, iso3.Point)
    assert iso_point.north == y
    assert iso_point.east == x


def test_to_shapely_point(converter):
    y, x = (Decimal(-89.9), Decimal(179.55))
    iso_point = iso3.Point(
        type=iso3.PointType.Other,
        north=y,
        east=x
    )
    shp_pnt = converter.to_shapely_point(iso_point)
    assert isinstance(shp_pnt, shp.Point)
    assert shp_pnt.x == x
    assert shp_pnt.y == y


def test_linestring(converter):
    ls = shp.LineString([[0, 0], [1, 0], [1, 1]])
    iso_ls = converter.to_iso_line_string(ls, iso3.LineStringType.PolygonExterior)
    assert isinstance(iso_ls, iso3.LineString)
    test_pnt = iso_ls.points[1]
    assert test_pnt.north == 0
    assert test_pnt.east == 1
    shp_ls = converter.to_shapely_line_string(iso_ls)
    assert shp_ls.equals(ls)


def test_polygon(converter):
    poly = shp.Polygon(
        shell=[[10, 0], [0, 0], [0, 10], [10, 0]],
        holes=[
            [[1, 1], [2, 1], [2, 2], [1, 1]],
            [[4, 4], [3, 4], [3, 3], [4, 4]]
        ]
    )
    iso_poly = converter.to_iso_polygon(poly)
    assert isinstance(iso_poly, iso3.Polygon)
    shp_poly = converter.to_shapely_polygon(iso_poly)
    assert shp_poly.equals(poly)


def test_multipoint(converter):
    multipoint = shp.MultiPoint([[0.0, 0.0], [1.0, 2.0]])
    iso_points = converter.to_iso_point_list(multipoint)
    assert isinstance(iso_points, list)
    assert isinstance(iso_points[0], iso3.Point)
    shp_multipoint = converter.to_shapely_multi_point(iso_points)
    assert shp_multipoint.equals(multipoint)


def test_multi_linestring(converter):
    multi_linestring = shp.MultiLineString([[[0, 0], [1, 2]], [[4, 4], [5, 6]]])
    iso_linestring_s = converter.to_iso_line_string_list(multi_linestring, iso3.LineStringType.SamplingRoute)
    assert isinstance(iso_linestring_s, list)
    assert isinstance(iso_linestring_s[0], iso3.LineString)
    shp_multi_linestring = converter.to_shapely_multi_line_string(iso_linestring_s)
    assert shp_multi_linestring.equals(multi_linestring)


def test_multi_polygon(converter):
    multi_polygon = shp.MultiPolygon([
        (((0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)),
         [((0.1, 0.1), (0.1, 0.2), (0.2, 0.2), (0.2, 0.1))])
    ])
    iso_polygon_s = converter.to_iso_polygon_list(multi_polygon)
    assert isinstance(iso_polygon_s, list)
    assert isinstance(iso_polygon_s[0], iso3.Polygon)
    shp_multi_polygon = converter.to_shapely_multi_polygon(iso_polygon_s)
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
