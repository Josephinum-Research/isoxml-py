from dataclasses import dataclass, field


@dataclass
class DeviceProperty:
    """
    DeviceProperty.

    :ivar object_id: A, (required)
    :ivar ddi: B, (required)
    :ivar value: C, (required)
    :ivar designator: D
    :ivar device_value_presentation_object_id: E
    """

    class Meta:
        name = "DPT"

    object_id: None | int = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "DevicePropertyObjectId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 65534,
        },
    )
    ddi: None | bytes = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "DevicePropertyDDI",
            "type": "Attribute",
            "required": True,
            "length": 2,
            "format": "base16",
        },
    )
    value: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "DevicePropertyValue",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "DevicePropertyDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    device_value_presentation_object_id: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "DeviceValuePresentationObjectId",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 65534,
        },
    )
