from dataclasses import dataclass, field
from enum import Enum


class TimeLogType(Enum):
    BinaryTimelogFileType1 = "1"


@dataclass
class TimeLog:
    """
    TimeLog.

    :ivar filename: A, (required)
    :ivar filelength: B
    :ivar type: C, (required)
    """

    class Meta:
        name = "TLG"

    filename: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "Filename",
            "type": "Attribute",
            "required": True,
            "length": 8,
            "pattern": r"TLG[0-9][0-9][0-9][0-9][0-9]",
        },
    )
    filelength: None | int = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "Filelength",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
    type: None | TimeLogType = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "TimeLogType",
            "type": "Attribute",
            "required": True,
        },
    )
