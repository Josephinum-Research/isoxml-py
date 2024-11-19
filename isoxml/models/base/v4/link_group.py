from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v4.link import Link


class LinkGroupB(Enum):
    UUIDs = '1'
    ManufacturerProprietary = '2'
    UniqueResolvableURIs = '3'
    InformationalResolvableURIs = '4'


@dataclass
class LinkGroup:
    """
    LinkGroup.

    :ivar links: LNK
    :ivar id: A, (required)
    :ivar type: B, (required)
    :ivar manufacturer_gln: C
    :ivar namespace: D
    :ivar designator: E
    """

    class Meta:
        name = "LGP"

    links: list[Link] = field(
        default_factory=list,
        metadata={
            "name": "LNK",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "LinkGroupId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(LGP|LGP-)([0-9])+",
        },
    )
    type: None | LinkGroupB = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "LinkGroupType",
            "type": "Attribute",
            "required": True,
        },
    )
    manufacturer_gln: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "ManufacturerGLN",
            "type": "Attribute",
            "max_length": 64,
        },
    )
    namespace: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "LinkGroupNamespace",
            "type": "Attribute",
            "max_length": 255,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "LinkGroupDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
