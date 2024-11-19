from dataclasses import dataclass, field

from isoxml.models.base.v3.allocation_stamp import AllocationStamp


@dataclass
class WorkerAllocation:
    """
    WorkerAllocation.

    :ivar allocation_stamp: ASP
    :ivar worker_id_ref: A, (required)
    """

    class Meta:
        name = "WAN"

    allocation_stamp: None | AllocationStamp = field(
        default=None,
        metadata={
            "name": "ASP",
            "full_name": "AllocationStamp",
            "type": "Element",
        },
    )
    worker_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "WorkerIdRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(WKR|WKR-)([0-9])+",
        },
    )
