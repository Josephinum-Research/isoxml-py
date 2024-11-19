from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum


class PositionStatus(Enum):
    NoGPSFix = "0",
    GNSSFix = "1",
    DGNSSFix = "2",
    PreciseGNSS = "3",
    RTKFixedInteger = "4",
    RTKFloat = "5",
    EstDRMode = "6",
    ManualInput = "7",
    SimulateMode = "8",
    Reserved9 = "9",
    Reserved10 = "10",
    Reserved11 = "11",
    Reserved12 = "12",
    Reserved13 = "13",
    Error = "14",
    PositionStatusValueIsNotAvailable = "15"


@dataclass
class Position:
    """
    Position.

    :ivar north: A, (required)
    :ivar east: B, (required)
    :ivar up: C
    :ivar status: D, (required)
    :ivar pdop: E
    :ivar hdop: F
    :ivar number_of_satellites: G
    :ivar gps_utc_time: H
    :ivar gps_utc_date: I
    """

    class Meta:
        name = "PTN"

    north: None | Decimal = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "PositionNorth",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-90.0"),
            "max_inclusive": Decimal("90.0"),
        },
    )
    east: None | Decimal = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "PositionEast",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-180.0"),
            "max_inclusive": Decimal("180.0"),
        },
    )
    up: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "PositionUp",
            "type": "Attribute",
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )
    status: None | PositionStatus = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "PositionStatus",
            "type": "Attribute",
            "required": True,
        },
    )
    pdop: None | Decimal = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "PDOP",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("99.9"),
        },
    )
    hdop: None | Decimal = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "HDOP",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("99.9"),
        },
    )
    number_of_satellites: None | int = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "NumberOfSatellites",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
    gps_utc_time: None | int = field(
        default=None,
        metadata={
            "name": "H",
            "full_name": "GpsUtcTime",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    gps_utc_date: None | int = field(
        default=None,
        metadata={
            "name": "I",
            "full_name": "GpsUtcDate",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 65534,
        },
    )
