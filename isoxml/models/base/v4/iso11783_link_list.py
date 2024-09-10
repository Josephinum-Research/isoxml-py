from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v4.link_group import LinkGroup


class Iso11783LinkListDataTransferOrigin(Enum):
    """
    :cvar FMIS: Farm Management Information Systems
    :cvar MICS: mobile implement control system
    """

    FMIS = "1"
    MICS = "2"


class Iso11783LinkListVersionMajor(Enum):
    """
    :cvar VALUE_4: The version of the second edition published as a
        Final Draft International Standard
    """

    VALUE_4 = "4"


class Iso11783LinkListVersionMinor(Enum):
    """
    All minor versions up to 3 of the XML schema for this major version.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


@dataclass
class Iso11783LinkList:
    """
    ISO 11783 Link List File.

    :ivar link_groups: LGP
    :ivar version_major: Version Major, (default: 4)
    :ivar version_minor: Version Minor, (default: 3)
    :ivar management_software_manufacturer: ManagementSoftwareManufacturer, (required)
    :ivar management_software_version: ManagementSoftwareVersion, (required)
    :ivar task_controller_manufacturer: TaskControllerManufacturer
    :ivar task_controller_version: TaskControllerVersion
    :ivar file_version: FileVersion
    :ivar data_transfer_origin: DataTransferOrigin, (required)
    """

    class Meta:
        name = "ISO11783LinkList"

    link_groups: list[LinkGroup] = field(
        default_factory=list,
        metadata={
            "name": "LGP",
            "type": "Element",
        },
    )
    version_major: Iso11783LinkListVersionMajor = field(
        init=False,
        default=Iso11783LinkListVersionMajor.VALUE_4,
        metadata={
            "name": "VersionMajor",
            "type": "Attribute",
            "required": True,
        },
    )
    version_minor: None | Iso11783LinkListVersionMinor = field(
        default=Iso11783LinkListVersionMinor.VALUE_3,
        metadata={
            "name": "VersionMinor",
            "type": "Attribute",
            "required": True,
        },
    )
    management_software_manufacturer: None | str = field(
        default=None,
        metadata={
            "name": "ManagementSoftwareManufacturer",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
    management_software_version: None | str = field(
        default=None,
        metadata={
            "name": "ManagementSoftwareVersion",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
    task_controller_manufacturer: None | str = field(
        default=None,
        metadata={
            "name": "TaskControllerManufacturer",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    task_controller_version: None | str = field(
        default=None,
        metadata={
            "name": "TaskControllerVersion",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    file_version: None | str = field(
        default=None,
        metadata={
            "name": "FileVersion",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    data_transfer_origin: None | Iso11783LinkListDataTransferOrigin = field(
        default=None,
        metadata={
            "name": "DataTransferOrigin",
            "type": "Attribute",
            "required": True,
        },
    )
