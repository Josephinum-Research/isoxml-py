from dataclasses import dataclass, field

from isoxml.models.base.v4.allocation_stamp import AllocationStamp


@dataclass
class ControlAssignment:
    """
    ControlAssignment.

    :ivar allocation_stamp: ASP
    :ivar source_client_name: A, (required)
    :ivar user_client_name: B, (required)
    :ivar source_device_structure_label: C, (required)
    :ivar user_device_structure_label: D, (required)
    :ivar source_device_element_number: E, (required)
    :ivar user_device_element_number: F, (required)
    :ivar process_data_ddi: G, (required)
    """

    class Meta:
        name = "CAT"

    allocation_stamp: None | AllocationStamp = field(
        default=None,
        metadata={
            "name": "ASP",
            "full_name": "AllocationStamp",
            "type": "Element",
        },
    )
    source_client_name: None | bytes = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "SourceClientNAME",
            "type": "Attribute",
            "required": True,
            "length": 8,
            "format": "base16",
        },
    )
    user_client_name: None | bytes = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "UserClientNAME",
            "type": "Attribute",
            "required": True,
            "length": 8,
            "format": "base16",
        },
    )
    source_device_structure_label: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "SourceDeviceStructureLabel",
            "type": "Attribute",
            "required": True,
            "min_length": 7,
            "max_length": 39,
            "pattern": r"((([0-9]|[a-e]|[A-E])([0-9]|[a-f]|[A-F]))|((F|f)([0-9]|[a-e]|[A-E]))){7}(([0-9]|[a-f]|[A-F])([0-9]|[a-f]|[A-F]))*",
            "format": "base16",
        },
    )
    user_device_structure_label: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "UserDeviceStructureLabel",
            "type": "Attribute",
            "required": True,
            "min_length": 7,
            "max_length": 39,
            "pattern": r"((([0-9]|[A-E]|[a-e])([0-9]|[A-F]|[a-f]))|((F|f)([0-9]|[A-E]|[a-e]))){7}(([0-9]|[A-F]|[a-f])([0-9]|[A-F]|[a-f]))*",
            "format": "base16",
        },
    )
    source_device_element_number: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "SourceDeviceElementNumber",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4095,
        },
    )
    user_device_element_number: None | int = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "UserDeviceElementNumber",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4095,
        },
    )
    process_data_ddi: None | bytes = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "ProcessDataDDI",
            "type": "Attribute",
            "required": True,
            "length": 2,
            "format": "base16",
        },
    )
