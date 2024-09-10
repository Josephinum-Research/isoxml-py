from dataclasses import dataclass, field


@dataclass
class DeviceObjectReference:
    """
    DeviceObjectReference.

    :ivar device_object_id: A, (required)
    """

    class Meta:
        name = "DOR"

    device_object_id: None | int = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "DeviceObjectId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 65534,
        },
    )
