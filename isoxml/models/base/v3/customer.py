from dataclasses import dataclass, field


@dataclass
class Customer:
    """
    Customer.

    :ivar id: A, (required)
    :ivar designator: B, (required)
    :ivar first_name: C
    :ivar street: D
    :ivar po_box: E
    :ivar postal_code: F
    :ivar city: G
    :ivar state: H
    :ivar country: I
    :ivar phone: J
    :ivar mobile: K
    :ivar fax: L
    :ivar e_mail: M
    """

    class Meta:
        name = "CTR"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "CustomerId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CTR|CTR-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "CustomerDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
    first_name: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "CustomerFirstName",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    street: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "CustomerStreet",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    po_box: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "CustomerPOBox",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    postal_code: None | str = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "CustomerPostalCode",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    city: None | str = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "CustomerCity",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    state: None | str = field(
        default=None,
        metadata={
            "name": "H",
            "full_name": "CustomerState",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "I",
            "full_name": "CustomerCountry",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    phone: None | str = field(
        default=None,
        metadata={
            "name": "J",
            "full_name": "CustomerPhone",
            "type": "Attribute",
            "max_length": 20,
        },
    )
    mobile: None | str = field(
        default=None,
        metadata={
            "name": "K",
            "full_name": "CustomerMobile",
            "type": "Attribute",
            "max_length": 20,
        },
    )
    fax: None | str = field(
        default=None,
        metadata={
            "name": "L",
            "full_name": "CustomerFax",
            "type": "Attribute",
            "max_length": 20,
        },
    )
    e_mail: None | str = field(
        default=None,
        metadata={
            "name": "M",
            "full_name": "CustomerEMail",
            "type": "Attribute",
            "max_length": 64,
        },
    )
