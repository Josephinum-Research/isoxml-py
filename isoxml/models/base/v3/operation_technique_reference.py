from dataclasses import dataclass, field


@dataclass
class OperationTechniqueReference:
    """
    OperationTechniqueReference.

    :ivar operation_technique_id_ref: A, (required)
    """

    class Meta:
        name = "OTR"

    operation_technique_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "OperationTechniqueIdRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(OTQ|OTQ-)([0-9])+",
        },
    )
