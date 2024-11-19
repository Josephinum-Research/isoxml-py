from dataclasses import dataclass, field


@dataclass
class CodedCommentListValue:
    """
    CodedCommentListValue.

    :ivar id: A, (required)
    :ivar designator: B, (required)
    """

    class Meta:
        name = "CCL"

    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "CodedCommentListValueId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CCL|CCL-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "CodedCommentListValueDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
