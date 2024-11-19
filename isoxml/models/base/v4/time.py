from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime

from isoxml.models.base.v4.data_log_value import DataLogValue
from isoxml.models.base.v4.position import Position


class TimeType(Enum):
    Planned = '1',
    Preliminary = '2',
    Effective = '4',
    Ineffective = '5',
    Repair = '6',
    Clearing = '7',
    PoweredDown = '8',


@dataclass
class Time:
    """
    Time.

    :ivar positions: PTN
    :ivar data_log_values: DLV
    :ivar start: A, (required)
    :ivar stop: B
    :ivar duration: C
    :ivar type: D, (required)
    """

    class Meta:
        name = "TIM"

    positions: list[Position] = field(
        default_factory=list,
        metadata={
            "name": "PTN",
            "full_name": "Position",
            "type": "Element",
        },
    )
    data_log_values: list[DataLogValue] = field(
        default_factory=list,
        metadata={
            "name": "DLV",
            "full_name": "DataLogValue",
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
    type: None | TimeType = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
