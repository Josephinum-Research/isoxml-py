from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from isoxml.models.base.v4.line_string import LineString
from isoxml.models.base.v4.polygon import Polygon


class GuidancePatternType(Enum):
    AB = '1'
    APlus = '2'
    Curve = '3'
    Pivot = '4'
    Spiral = '5'


class GuidancePatternOptions(Enum):
    ClockwiseForPivot = '1'
    CounterClockwiseForPivot = '2'
    FullCircleForPivot = '3'


class GuidancePatternPropagationDirection(Enum):
    BothDirections = '1'
    LeftDirectionOnly = '2'
    RightDirectionOnly = '3'
    NoPropagation = '4'


class GuidancePatternExtension(Enum):
    FromBothFirstAndLastPoint = '1'
    FromFirstPointAOnly = '2'
    FromLastPointBOnly = '3'
    NoExtensions = '4'


class GuidancePatternGNSSMethod(Enum):
    NoGPSFix = '0'
    GNSSFix = '1'
    DGNSSFix = '2'
    PreciseGNSS = '3'
    RTKFixedInteger = '4'
    RTKFloat = '5'
    EstDRMode = '6'
    ManualInput = '7'
    SimulateMode = '8'
    DesktopGeneratedData = '16'
    Other = '17'


@dataclass
class GuidancePattern:
    """
    GuidancePattern.

    :ivar line_strings: LSG
    :ivar boundary_polygons: PLN
    :ivar id: A, (required)
    :ivar designator: B
    :ivar type: C, (required)
    :ivar options: D
    :ivar propagation_direction: E
    :ivar extension: F
    :ivar heading: G
    :ivar radius: H
    :ivar gnss_method: I
    :ivar horizontal_accuracy: J
    :ivar vertical_accuracy: K
    :ivar base_station_id_ref: L
    :ivar original_srid: M
    :ivar number_of_swaths_left: N
    :ivar number_of_swaths_right: O
    """

    class Meta:
        name = "GPN"

    line_strings: list[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LSG",
            "full_name": "LineString",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1,
        },
    )
    boundary_polygons: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "PLN",
            "full_name": "BoundaryPolygon",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "GuidancePatternId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(GPN|GPN-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "GuidancePatternDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    type: None | GuidancePatternType = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "GuidancePatternType",
            "type": "Attribute",
            "required": True,
        },
    )
    options: None | GuidancePatternOptions = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "GuidancePatternOptions",
            "type": "Attribute",
        },
    )
    propagation_direction: None | GuidancePatternPropagationDirection = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "GuidancePatternPropagationDirection",
            "type": "Attribute",
        },
    )
    extension: None | GuidancePatternExtension = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "GuidancePatternExtension",
            "type": "Attribute",
        },
    )
    heading: None | Decimal = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "GuidancePatternHeading",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("360.0"),
        },
    )
    radius: None | int = field(
        default=None,
        metadata={
            "name": "H",
            "full_name": "GuidancePatternRadius",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    gnss_method: None | GuidancePatternGNSSMethod = field(
        default=None,
        metadata={
            "name": "I",
            "full_name": "GuidancePatternGNSSMethod",
            "type": "Attribute",
        },
    )
    horizontal_accuracy: None | Decimal = field(
        default=None,
        metadata={
            "name": "J",
            "full_name": "GuidancePatternHorizontalAccuracy",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("65.0"),
        },
    )
    vertical_accuracy: None | Decimal = field(
        default=None,
        metadata={
            "name": "K",
            "full_name": "GuidancePatternVerticalAccuracy",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("65.0"),
        },
    )
    base_station_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "L",
            "full_name": "BaseStationIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(BSN|BSN-)([0-9])+",
        },
    )
    original_srid: None | str = field(
        default=None,
        metadata={
            "name": "M",
            "full_name": "OriginalSRID",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    number_of_swaths_left: None | int = field(
        default=None,
        metadata={
            "name": "N",
            "full_name": "NumberOfSwathsLeft",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    number_of_swaths_right: None | int = field(
        default=None,
        metadata={
            "name": "O",
            "full_name": "NumberOfSwathsRight",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
