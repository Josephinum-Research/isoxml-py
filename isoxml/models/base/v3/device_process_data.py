from dataclasses import dataclass, field


@dataclass
class DeviceProcessData:
    """
    DeviceProcessData.

    :ivar object_id: A, (required)
    :ivar ddi: B, (required)
    :ivar property: C, (required)
    :ivar trigger_methods: D, (required)
    :ivar designator: E
    :ivar device_value_presentation_object_id: F
    """

    class Meta:
        name = "DPD"

    object_id: None | int = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "DeviceProcessDataObjectId",
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
            "full_name": "DeviceProcessDataDDI",
            "type": "Attribute",
            "required": True,
            "length": 2,
            "format": "base16",
        },
    )
    property: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "DeviceProcessDataProperty",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 3,
        },
    )
    trigger_methods: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "DeviceProcessDataTriggerMethods",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "DeviceProcessDataDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    device_value_presentation_object_id: None | int = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "DeviceValuePresentationObjectId",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 65534,
        },
    )
