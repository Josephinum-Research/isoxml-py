from dataclasses import dataclass, field
from enum import Enum


class ExternalFileReferenceB(Enum):
    XML = "1"


@dataclass
class ExternalFileReference:
    """
    ExternalFileReference.

    :ivar filename: A, (required)
    :ivar filetype: B, (required)
    """

    class Meta:
        name = "XFR"

    filename: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "Filename",
            "type": "Attribute",
            "required": True,
            "length": 8,
            "pattern": r"(BSN|CCG|CCT|CLD|CPC|CTP|CTR|DVC|FRM|OTQ|PDT|PFD|PGP|TSK|VPN|WKR)[0-9][0-9][0-9][0-9][0-9]",
        },
    )
    filetype: None | ExternalFileReferenceB = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "Filetype",
            "type": "Attribute",
            "required": True,
        },
    )
