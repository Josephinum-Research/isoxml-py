from dataclasses import dataclass, field


@dataclass
class Connection:
    """
    Connection.

    :ivar device_id_ref_0: A, (required)
    :ivar device_element_id_ref_0: B, (required)
    :ivar device_id_ref_1: C, (required)
    :ivar device_element_id_ref_1: D, (required)
    """

    class Meta:
        name = "CNN"

    device_id_ref_0: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "DeviceIdRef_0",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(DVC|DVC-)([0-9])+",
        },
    )
    device_element_id_ref_0: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "DeviceElementIdRef_0",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(DET|DET-)([0-9])+",
        },
    )
    device_id_ref_1: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "DeviceIdRef_1",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(DVC|DVC-)([0-9])+",
        },
    )
    device_element_id_ref_1: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "DeviceElementIdRef_1",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(DET|DET-)([0-9])+",
        },
    )
