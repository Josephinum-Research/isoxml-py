from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime

from isoxml.models.base.v3.position import Position


class AllocationStampType(Enum):
    Planned = "1"
    Effective = "4"


@dataclass
class AllocationStamp:
    """
    AllocationStamp.

    :ivar position: PTN
    :ivar start: A, (required)
    :ivar stop: B
    :ivar duration: C
    :ivar type: D, (required)
    """

    class Meta:
        name = "ASP"

    position: None | Position = field(
        default=None,
        metadata={
            "name": "PTN",
            "full_name": "Position",
            "type": "Element",
        },
    )
    start: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "Start",
            "type": "Attribute",
            "required": True,
        },
    )
    stop: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "Stop",
            "type": "Attribute",
        },
    )
    duration: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "Duration",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    type: None | AllocationStampType = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
