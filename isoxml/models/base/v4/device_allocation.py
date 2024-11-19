from dataclasses import dataclass, field

from isoxml.models.base.v4.allocation_stamp import AllocationStamp


@dataclass
class DeviceAllocation:
    """
    DeviceAllocation.

    :ivar allocation_stamp: ASP
    :ivar client_name_value: A, (required)
    :ivar client_name_mask: B
    :ivar device_id_ref: C
    """

    class Meta:
        name = "DAN"

    allocation_stamp: None | AllocationStamp = field(
        default=None,
        metadata={
            "name": "ASP",
            "full_name": "AllocationStamp",
            "type": "Element",
        },
    )
    client_name_value: None | bytes = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "ClientNAMEValue",
            "type": "Attribute",
            "required": True,
            "length": 8,
            "format": "base16",
        },
    )
    client_name_mask: None | bytes = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "ClientNAMEMask",
            "type": "Attribute",
            "length": 8,
            "format": "base16",
        },
    )
    device_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "DeviceIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(DVC|DVC-)([0-9])+",
        },
    )
