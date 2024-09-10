from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v4.product_relation import ProductRelation


class ProductF(Enum):
    Single = "1"
    Mixture = "2"
    TemporaryMixture = "3"


@dataclass
class Product:
    """
    Product.

    :ivar relations: PRN
    :ivar id: A, (required)
    :ivar designator: B, (required)
    :ivar group_id_ref: C
    :ivar value_presentation_id_ref: D
    :ivar quantity_ddi: E
    :ivar type: F
    :ivar mixture_recipe_quantity: G
    :ivar density_mass_per_volume: H
    :ivar density_mass_per_count: I
    :ivar density_volume_per_count: J
    """

    class Meta:
        name = "PDT"

    relations: list[ProductRelation] = field(
        default_factory=list,
        metadata={
            "name": "PRN",
            "full_name": "ProductRelation",
            "type": "Element",
        },
    )
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
    quantity_ddi: None | bytes = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "QuantityDDI",
            "type": "Attribute",
            "length": 2,
            "format": "base16",
        },
    )
    type: None | ProductF = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "ProductType",
            "type": "Attribute",
        },
    )
    mixture_recipe_quantity: None | int = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "MixtureRecipeQuantity",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )
    density_mass_per_volume: None | int = field(
        default=None,
        metadata={
            "name": "H",
            "full_name": "DensityMassPerVolume",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )
    density_mass_per_count: None | int = field(
        default=None,
        metadata={
            "name": "I",
            "full_name": "DensityMassPerCount",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )
    density_volume_per_count: None | int = field(
        default=None,
        metadata={
            "name": "J",
            "full_name": "DensityVolumePerCount",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 2147483647,
        },
    )
