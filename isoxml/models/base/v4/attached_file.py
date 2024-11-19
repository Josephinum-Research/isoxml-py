from dataclasses import dataclass, field
from enum import Enum


class AttachedFilePreserve(Enum):
    TaskControllerDoesNotNeedToPreserveAttachedFile = "1"
    PreserveOnTaskControllerAndSendBackToFMIS = "2"


@dataclass
class AttachedFile:
    """
    AttachedFile.

    :ivar filename_with_extension: A, (required)
    :ivar preserve: B, (required)
    :ivar manufacturer_gln: C, (required)
    :ivar file_type: D, (required)
    :ivar file_version: E
    :ivar file_length: F
    """

    class Meta:
        name = "AFE"

    filename_with_extension: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "FilenameWithExtension",
            "type": "Attribute",
            "required": True,
            "length": 12,
            "pattern": r"([0-9]|[A-Z]){8}.([0-9]|[A-Z]){3}",
        },
    )
    preserve: None | AttachedFilePreserve = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "Preserve",
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
            "required": True,
            "max_length": 32,
        },
    )
    file_type: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "FileType",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 254,
        },
    )
    file_version: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "FileVersion",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    file_length: None | int = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "FileLength",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 4294967294,
        },
    )
