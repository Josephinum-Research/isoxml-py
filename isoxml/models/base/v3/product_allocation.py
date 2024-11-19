from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v3.allocation_stamp import AllocationStamp


class ProductAllocationTransferMode(Enum):
    Filling = "1"
    Emptying = "2"


@dataclass
class ProductAllocation:
    """
    ProductAllocation.

    :ivar asp: ASP
    :ivar product_id_ref: A, (required)
    :ivar amount_ddi: B
    :ivar amount_value: C
    :ivar transfer_mode: D
    :ivar device_element_id_ref: E
    :ivar value_presentation_id_ref: F
    """

    class Meta:
        name = "PAN"

    asp: None | AllocationStamp = field(
        default=None,
        metadata={
            "name": "ASP",
            "type": "Element",
        },
    )
    product_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "ProductIdRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(PDT|PDT-)([0-9])+",
        },
    )
    amount_ddi: None | bytes = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "AmountDDI",
            "type": "Attribute",
            "length": 2,
            "format": "base16",
        },
    )
    amount_value: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "AmountValue",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )
    transfer_mode: None | ProductAllocationTransferMode = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "TransferMode",
            "type": "Attribute",
        },
    )
    device_element_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "DeviceElementIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(DET|DET-)([0-9])+",
        },
    )
    value_presentation_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "ValuePresentationIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(VPN|VPN-)([0-9])+",
        },
    )
