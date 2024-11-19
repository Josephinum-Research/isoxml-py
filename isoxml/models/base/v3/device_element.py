from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v3.device_object_reference import DeviceObjectReference


class DeviceElementType(Enum):
    Device = "1"
    Function = "2"
    Bin = "3"
    Section = "4"
    Unit = "5"
    Connector = "6"
    Navigation = "7"


@dataclass
class DeviceElement:
    """
    DeviceElement.

    :ivar device_object_references: DOR
    :ivar id: A, (required)
    :ivar object_id: B, (required)
    :ivar type: C, (required)
    :ivar designator: D
    :ivar number: E, (required)
    :ivar parent_object_id: F, (required)
    """

    class Meta:
        name = "DET"

    device_object_references: list[DeviceObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "DOR",
            "full_name": "DeviceObjectReference",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "DeviceElementId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(DET|DET-)([0-9])+",
        },
    )
    object_id: None | int = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "DeviceElementObjectId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 65534,
        },
    )
    type: None | DeviceElementType = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "DeviceElementType",
            "type": "Attribute",
            "required": True,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "DeviceElementDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    number: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "DeviceElementNumber",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4095,
        },
    )
    parent_object_id: None | int = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "ParentObjectId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 65534,
        },
    )
