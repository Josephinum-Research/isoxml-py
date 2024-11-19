from dataclasses import dataclass, field


@dataclass
class Worker:
    """
    Worker.

    :ivar id: A, (required)
    :ivar last_name: B, (required)
    :ivar first_name: C
    :ivar street: D
    :ivar po_box: E
    :ivar postal_code: F
    :ivar city: G
    :ivar state: H
    :ivar country: I
    :ivar phone: J
    :ivar mobile: K
    :ivar license_number: L
    :ivar e_mail: M
    """

    class Meta:
        name = "WKR"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "WorkerId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(WKR|WKR-)([0-9])+",
        },
    )
    last_name: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "WorkerLastName",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
    first_name: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "WorkerFirstName",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    street: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "WorkerStreet",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    po_box: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "WorkerPOBox",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    postal_code: None | str = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "WorkerPostalCode",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    city: None | str = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "WorkerCity",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    state: None | str = field(
        default=None,
        metadata={
            "name": "H",
            "full_name": "WorkerState",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "I",
            "full_name": "WorkerCountry",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    phone: None | str = field(
        default=None,
        metadata={
            "name": "J",
            "full_name": "WorkerPhone",
            "type": "Attribute",
            "max_length": 20,
        },
    )
    mobile: None | str = field(
        default=None,
        metadata={
            "name": "K",
            "full_name": "WorkerMobile",
            "type": "Attribute",
            "max_length": 20,
        },
    )
    license_number: None | str = field(
        default=None,
        metadata={
            "name": "L",
            "full_name": "WorkerLicenseNumber",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    e_mail: None | str = field(
        default=None,
        metadata={
            "name": "M",
            "full_name": "WorkerEMail",
            "type": "Attribute",
            "max_length": 64,
        },
    )
