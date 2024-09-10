from dataclasses import dataclass, field


@dataclass
class ProductRelation:
    """
    ProductRelation.

    :ivar product_id_ref: A, (required)
    :ivar quantity_value: B, (required)
    """

    class Meta:
        name = "PRN"

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
    quantity_value: None | int = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "QuantityValue",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )
