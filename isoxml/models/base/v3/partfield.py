from dataclasses import dataclass, field

from isoxml.models.base.v3.line_string import LineString
from isoxml.models.base.v3.polygon import Polygon
from isoxml.models.base.v3.point import Point


@dataclass
class Partfield:
    """
    Partfield.

    :ivar polygons: PLN
    :ivar line_strings: LSG
    :ivar points: PNT
    :ivar id: A, (required)
    :ivar code: B
    :ivar designator: C, (required)
    :ivar area: D, (required)
    :ivar customer_id_ref: E
    :ivar farm_id_ref: F
    :ivar crop_type_id_ref: G
    :ivar crop_variety_id_ref: H
    :ivar field_id_ref: I
    """

    class Meta:
        name = "PFD"

    polygons: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "PLN",
            "full_name": "Polygon",
            "type": "Element",
        },
    )
    line_strings: list[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LSG",
            "full_name": "Linestring",
            "type": "Element",
        },
    )
    points: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "PNT",
            "full_name": "Point",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "PartfieldId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(PFD|PFD-)([0-9])+",
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "PartfieldCode",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "PartfieldDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
    area: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "PartfieldArea",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    customer_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "CustomerIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CTR|CTR-)([0-9])+",
        },
    )
    farm_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "FarmIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(FRM|FRM-)([0-9])+",
        },
    )
    crop_type_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "CropTypeIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CTP|CTP-)([0-9])+",
        },
    )
    crop_variety_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "H",
            "full_name": "CropVarietyIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CVT|CVT-)([0-9])+",
        },
    )
    field_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "I",
            "full_name": "FieldIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(PFD|PFD-)([0-9])+",
        },
    )
