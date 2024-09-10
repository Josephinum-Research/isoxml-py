from dataclasses import dataclass, field


@dataclass
class Farm:
    """
    Farm.

    :ivar id: A, (required)
    :ivar designator: B, (required)
    :ivar street: C
    :ivar po_box: D
    :ivar postal_code: E
    :ivar city: F
    :ivar state: G
    :ivar country: H
    :ivar customer_id_ref: I
    """

    class Meta:
        name = "FRM"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "FarmId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(FRM|FRM-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "FarmDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
    street: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "FarmStreet",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    po_box: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "FarmPOBox",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    postal_code: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "FarmPostalCode",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    city: None | str = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "FarmCity",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    state: None | str = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "FarmState",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "H",
            "full_name": "FarmCountry",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    customer_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "I",
            "full_name": "CustomerIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CTR|CTR-)([0-9])+",
        },
    )
