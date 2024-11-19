from dataclasses import dataclass, field

from isoxml.models.base.v4.process_data_variable import ProcessDataVariable
from isoxml.models.base.v4.polygon import Polygon


@dataclass
class TreatmentZone:
    """
    TreatmentZone.

    :ivar polygons: PLN
    :ivar process_data_variables: PDV
    :ivar code: A, (required)
    :ivar designator: B
    :ivar colour: C
    """

    class Meta:
        name = "TZN"

    polygons: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "PLN",
            "full_name": "Polygon",
            "type": "Element",
        },
    )
    process_data_variables: list[ProcessDataVariable] = field(
        default_factory=list,
        metadata={
            "name": "PDV",
            "full_name": "ProcessDataVariable",
            "type": "Element",
        },
    )
    code: None | int = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "TreatmentZoneCode",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "TreatmentZoneDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    colour: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "TreatmentZoneColour",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
