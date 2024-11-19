from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v3.coded_comment_list_value import CodedCommentListValue


class CodedCommentScope(Enum):
    Point = "1"
    Global = "2"
    Continuous = "3"


@dataclass
class CodedComment:
    """
    CodedComment.

    :ivar list_values: CCL
    :ivar id: A, (required)
    :ivar designator: B, (required)
    :ivar scope: C, (required)
    :ivar group_id_ref: D
    """

    class Meta:
        name = "CCT"

    list_values: list[CodedCommentListValue] = field(
        default_factory=list,
        metadata={
            "name": "CCL",
            "full_name": "CodedCommentListValue",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "CodedCommentId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CCT|CCT-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "CodedCommentDesignator",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        },
    )
    scope: None | CodedCommentScope = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "CodedCommentScope",
            "type": "Attribute",
            "required": True,
        },
    )
    group_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "CodedCommentGroupIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CCG|CCG-)([0-9])+",
        },
    )
