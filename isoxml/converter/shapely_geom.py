from decimal import Decimal
from types import ModuleType
from typing import Literal

import shapely as shp

import isoxml.models.base.v3 as iso3
import isoxml.models.base.v4 as iso4


class ShapelyConverter:
    def __init__(self, version: Literal['v3', 'v4']):
        self.iso: ModuleType
        match version:
            case 'v3':
                self.iso = iso3
            case 'v4':
                self.iso = iso4
            case _:
                raise NotImplementedError('only the conversion to v3 or v4 is supported')

    def _iso_point_from_coords(
            self, east: float, nord: float, pnt_type=None, **kwargs
    ):
        if pnt_type is None:
            pnt_type = self.iso.PointType.Other
        return self.iso.Point(
            type=pnt_type,
            north=round(Decimal(nord), 9),
            east=round(Decimal(east), 9),
            **kwargs
        )

    def to_iso_point(self, point: shp.Point, pnt_type=None, **kwargs):
        if pnt_type is None:
            pnt_type = self.iso.PointType.Other
        return self._iso_point_from_coords(
            east=point.x,
            nord=point.y,
            pnt_type=pnt_type,
            **kwargs
        )

    @staticmethod
    def to_shapely_point(iso_pnt) -> shp.Point:
        return shp.Point(iso_pnt.east, iso_pnt.north)

    def to_iso_line_string(
            self, line: shp.LineString, line_type, **kwargs
    ):
        return self.iso.LineString(
            type=line_type,
            points=[self._iso_point_from_coords(east=x, nord=y) for x, y in line.coords],
            **kwargs
        )

    @staticmethod
    def to_shapely_line_string(iso_line) -> shp.LineString:
        return shp.LineString(coordinates=[[iso_pnt.east, iso_pnt.north] for iso_pnt in iso_line.points])

    def to_iso_polygon(
            self, shp_polygon: shp.Polygon, poly_type=None, **kwargs
    ):
        if poly_type is None:
            poly_type = self.iso.PolygonType.Other
        shell = self.to_iso_line_string(shp_polygon.exterior, self.iso.LineStringType.PolygonExterior)
        inner = [self.to_iso_line_string(shp_ls, self.iso.LineStringType.PolygonInterior) for shp_ls in
                 shp_polygon.interiors]
        return self.iso.Polygon(
            type=poly_type,
            line_strings=[shell] + inner,
            **kwargs
        )

    def to_shapely_polygon(self, iso_polygon) -> shp.Polygon:
        holes = []
        shell = None
        for iso_ls in iso_polygon.line_strings:
            shp_ls = self.to_shapely_line_string(iso_ls)
            match iso_ls.type:
                case iso3.LineStringType.PolygonExterior | iso4.LineStringType.PolygonExterior:
                    shell = shp_ls
                case iso3.LineStringType.PolygonInterior | iso4.LineStringType.PolygonInterior:
                    holes.append(shp_ls)
                case _:
                    raise ValueError(f"linestring type {iso_ls.type} is not a valid type for a polygon component")
        if not shell:
            raise ValueError("provides isoxml polygon did not contain a PolygonExterior")
        return shp.Polygon(
            shell=shell,
            holes=holes
        )

    def to_iso_point_list(
            self, multi_point: shp.MultiPoint, pnt_type=None, **kwargs
    ) -> list:
        if pnt_type is None:
            pnt_type = self.iso.PointType.Other
        return [self.to_iso_point(shp_point, pnt_type, **kwargs) for shp_point in multi_point.geoms]

    def to_shapely_multi_point(self, iso_points: list) -> shp.MultiPoint:
        return shp.MultiPoint([self.to_shapely_point(iso_point) for iso_point in iso_points])

    def to_iso_line_string_list(
            self, multi_line: shp.MultiLineString, lsg_type, **kwargs
    ) -> list:
        return [
            self.to_iso_line_string(shp_line, lsg_type, **kwargs)
            for shp_line in multi_line.geoms
        ]

    def to_shapely_multi_line_string(self, iso_lines: list) -> shp.MultiLineString:
        return shp.MultiLineString([
            self.to_shapely_line_string(iso_line)
            for iso_line in iso_lines
        ])

    def to_iso_polygon_list(
            self, multi_polygon: shp.MultiPolygon, pln_type=None, **kwargs
    ) -> list:
        if pln_type is None:
            pln_type = self.iso.PolygonType.Other
        return [
            self.to_iso_polygon(shp_polygon, pln_type, **kwargs)
            for shp_polygon in multi_polygon.geoms
        ]

    def to_shapely_multi_polygon(self, iso_polygons: list) -> shp.MultiPolygon:
        return shp.MultiPolygon([
            self.to_shapely_polygon(iso_polygon)
            for iso_polygon in iso_polygons
        ])
