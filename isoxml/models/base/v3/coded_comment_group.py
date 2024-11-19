from dataclasses import dataclass, field


@dataclass
class CodedCommentGroup:
    """
    CodedCommentGroup.

    :ivar id: A, (required)
    :ivar designator: B, (required)
    """

    class Meta:
        name = "CCG"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "CodedCommentGroupId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CCG|CCG-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "CodedCommentGroupDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
