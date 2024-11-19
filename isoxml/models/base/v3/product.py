from dataclasses import dataclass, field


@dataclass
class Product:
    """
    Product.

    :ivar id: A, (required)
    :ivar designator: B, (required)
    :ivar group_id_ref: C
    :ivar value_presentation_id_ref: D
    :ivar amount_ddi: E
    """

    class Meta:
        name = "PDT"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "ProductId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(PDT|PDT-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "ProductDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
    group_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "ProductGroupIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(PGP|PGP-)([0-9])+",
        },
    )
    value_presentation_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "ValuePresentationIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(VPN|VPN-)([0-9])+",
        },
    )
    amount_ddi: None | bytes = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "AmountDDI",
            "type": "Attribute",
            "length": 2,
            "format": "base16",
        },
    )
