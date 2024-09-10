from dataclasses import dataclass, field
from enum import Enum


class TaskControllerCapabilitiesC(Enum):
    """
    :cvar DIS_1: The version of the DIS.1 (first draft international
        standard)
    :cvar FDIS_1: The version of the FDIS.1 (final draft international
        standard, first edition)
    :cvar FDIS_2: The version of the FDIS.2 and the first edition
        published as an international standard
    :cvar E2_DIS: The version of the second edition published as a
        draft international standard (E2.DIS)
    :cvar E2_FDIS: The version of the second edition published as a
        final draft international standard (E2.FDIS)
    """

    DIS_1 = "0"
    FDIS_1 = "1"
    FDIS_2 = "2"
    E2_DIS = "3"
    E2_FDIS = "4"


@dataclass
class TaskControllerCapabilities:
    """
    TaskControllerCapabilities.

    :ivar task_controller_control_function_name: A, (required)
    :ivar task_controller_designator: B, (required)
    :ivar version_number: C, (required)
    :ivar provided_capabilities: D, (required)
    :ivar number_of_booms_section_control: E, (required)
    :ivar number_of_sections_section_control: F, (required)
    :ivar number_of_control_channels: G, (required)
    """

    class Meta:
        name = "TCC"

    task_controller_control_function_name: None | bytes = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "TaskControllerControlFunctionNAME",
            "type": "Attribute",
            "required": True,
            "length": 8,
            "format": "base16",
        },
    )
    task_controller_designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "TaskControllerDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 153,
        },
    )
    version_number: None | TaskControllerCapabilitiesC = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "VersionNumber",
            "type": "Attribute",
            "required": True,
        },
    )
    provided_capabilities: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "ProvidedCapabilities",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 63,
        },
    )
    number_of_booms_section_control: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "NumberOfBoomsSectionControl",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
    number_of_sections_section_control: None | int = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "NumberOfSectionsSectionControl",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
    number_of_control_channels: None | int = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "NumberOfControlChannels",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
