from dataclasses import dataclass, field

from isoxml.models.base.v4.device_element import DeviceElement
from isoxml.models.base.v4.device_process_data import DeviceProcessData
from isoxml.models.base.v4.device_property import DeviceProperty
from isoxml.models.base.v4.device_value_presentation import DeviceValuePresentation


@dataclass
class Device:
    """
    Device.

    :ivar elements: DET
    :ivar properties: DPT
    :ivar process_data: DPD
    :ivar value_presentations: DVP
    :ivar id: A, (required)
    :ivar designator: B
    :ivar software_version: C
    :ivar client_name: D, (required)
    :ivar serial_number: E
    :ivar structure_label: F, (required)
    :ivar localization_label: G, (required)
    """

    class Meta:
        name = "DVC"

    elements: list[DeviceElement] = field(
        default_factory=list,
        metadata={
            "name": "DET",
            "full_name": "DeviceElement",
            "type": "Element",
        },
    )
    properties: list[DeviceProperty] = field(
        default_factory=list,
        metadata={
            "name": "DPT",
            "full_name": "DeviceProperty",
            "type": "Element",
        },
    )
    process_data: list[DeviceProcessData] = field(
        default_factory=list,
        metadata={
            "name": "DPD",
            "full_name": "DeviceProcessData",
            "type": "Element",
        },
    )
    value_presentations: list[DeviceValuePresentation] = field(
        default_factory=list,
        metadata={
            "name": "DVP",
            "full_name": "DeviceValuePresentation",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "DeviceId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(DVC|DVC-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "DeviceDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    software_version: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "DeviceSoftwareVersion",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    client_name: None | bytes = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "ClientNAME",
            "type": "Attribute",
            "required": True,
            "length": 8,
            "format": "base16",
        },
    )
    serial_number: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "DeviceSerialNumber",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    structure_label: None | str = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "DeviceStructureLabel",
            "type": "Attribute",
            "required": True,
            "min_length": 7,
            "max_length": 39,
            "pattern": r"((([0-9]|[a-e]|[A-E])([0-9]|[a-f]|[A-F]))|((F|f)([0-9]|[a-e]|[A-E]))){7}(([0-9]|[a-f]|[A-F])([0-9]|[a-f]|[A-F]))*",
            "format": "base16",
        },
    )
    localization_label: None | str = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "DeviceLocalizationLabel",
            "type": "Attribute",
            "required": True,
            "length": 7,
            "pattern": r"(F|f){2}((([0-9]|[A-E]|[a-e])([0-9]|[A-F]|[a-f]))|((F|f)([0-9]|[A-E]|[a-e])))*",
            "format": "base16",
        },
    )
