from dataclasses import dataclass, field

from isoxml.models.base.v3.allocation_stamp import AllocationStamp


@dataclass
class CommentAllocation:
    """
    CommentAllocation.

    :ivar allocation_stamp: ASP
    :ivar coded_comment_id_ref: A
    :ivar coded_comment_list_value_id_ref: B
    :ivar free_comment_text: C
    """

    class Meta:
        name = "CAN"

    allocation_stamp: None | AllocationStamp = field(
        default=None,
        metadata={
            "name": "ASP",
            "full_name": "AllocationStamp",
            "type": "Element",
        },
    )
    coded_comment_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "CodedCommentIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CCT|CCT-)([0-9])+",
        },
    )
    coded_comment_list_value_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "CodedCommentListValueIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CCL|CCL-)([0-9])+",
        },
    )
    free_comment_text: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "FreeCommentText",
            "type": "Attribute",
            "max_length": 32,
        },
    )
