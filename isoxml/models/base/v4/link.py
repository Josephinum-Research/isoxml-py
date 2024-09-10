from dataclasses import dataclass, field


@dataclass
class Link:
    """
    Link.

    :ivar object_id_ref: A, (required)
    :ivar value: B, (required)
    :ivar designator: C
    """

    class Meta:
        name = "LNK"

    object_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "ObjectIdRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(BSN|CCT|CCG|CCL|CLD|CTP|CVT|CPC|CTR|DET|DVC|FRM|GGP|GPN|LSG|OTQ|PFD|PNT|PLN|PDT|PGP|TSK|VPN|WKR)(|-)([0-9])+",
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "LinkValue",
            "type": "Attribute",
            "required": True,
            "max_length": 255,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "LinkDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
