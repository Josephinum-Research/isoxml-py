from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v3.comment_allocation import CommentAllocation
from isoxml.models.base.v3.connection import Connection
from isoxml.models.base.v3.data_log_trigger import DataLogTrigger
from isoxml.models.base.v3.device_allocation import DeviceAllocation
from isoxml.models.base.v3.grid import Grid
from isoxml.models.base.v3.oper_tech_practice import OperTechPractice
from isoxml.models.base.v3.product_allocation import ProductAllocation
from isoxml.models.base.v3.time import Time
from isoxml.models.base.v3.time_log import TimeLog
from isoxml.models.base.v3.treatment_zone import TreatmentZone
from isoxml.models.base.v3.worker_allocation import WorkerAllocation


class TaskStatus(Enum):
    Initial = "1"
    Running = "2"
    Paused = "3"
    Finished = "4"


@dataclass
class Task:
    """
    Task.

    :ivar treatment_zones: TZN
    :ivar times: TIM
    :ivar oper_tech_practices: OTP
    :ivar worker_allocations: WAN
    :ivar device_allocations: DAN
    :ivar connections: CNN
    :ivar product_allocations: PAN
    :ivar data_log_triggers: DLT
    :ivar comment_allocations: CAN
    :ivar time_logs: TLG
    :ivar grids: GRD
    :ivar id: A, (required)
    :ivar designator: B
    :ivar customer_id_ref: C
    :ivar farm_id_ref: D
    :ivar partfield_id_ref: E
    :ivar responsible_worker_id_ref: F
    :ivar status: G, (required)
    :ivar default_treatment_zone_code: H
    :ivar position_lost_treatment_zone_code: I
    :ivar out_of_field_treatment_zone_code: J
    """

    class Meta:
        name = "TSK"

    treatment_zones: list[TreatmentZone] = field(
        default_factory=list,
        metadata={
            "name": "TZN",
            "full_name": "TreatmentZone",
            "type": "Element",
        },
    )
    times: list[Time] = field(
        default_factory=list,
        metadata={
            "name": "TIM",
            "full_name": "Time",
            "type": "Element",
        },
    )
    oper_tech_practices: list[OperTechPractice] = field(
        default_factory=list,
        metadata={
            "name": "OTP",
            "full_name": "OperTechPractice",
            "type": "Element",
        },
    )
    worker_allocations: list[WorkerAllocation] = field(
        default_factory=list,
        metadata={
            "name": "WAN",
            "full_name": "WorkerAllocation",
            "type": "Element",
        },
    )
    device_allocations: list[DeviceAllocation] = field(
        default_factory=list,
        metadata={
            "name": "DAN",
            "full_name": "DeviceAllocation",
            "type": "Element",
        },
    )
    connections: list[Connection] = field(
        default_factory=list,
        metadata={
            "name": "CNN",
            "full_name": "Connection",
            "type": "Element",
        },
    )
    product_allocations: list[ProductAllocation] = field(
        default_factory=list,
        metadata={
            "name": "PAN",
            "full_name": "ProductAllocation",
            "type": "Element",
        },
    )
    data_log_triggers: list[DataLogTrigger] = field(
        default_factory=list,
        metadata={
            "name": "DLT",
            "full_name": "DataLogTrigger",
            "type": "Element",
        },
    )
    comment_allocations: list[CommentAllocation] = field(
        default_factory=list,
        metadata={
            "name": "CAN",
            "full_name": "CommentAllocation",
            "type": "Element",
        },
    )
    time_logs: list[TimeLog] = field(
        default_factory=list,
        metadata={
            "name": "TLG",
            "full_name": "TimeLog",
            "type": "Element",
        },
    )
    grids: list[Grid] = field(
        default_factory=list,
        metadata={
            "name": "GRD",
            "full_name": "Grid",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "TaskId",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(TSK|TSK-)([0-9])+",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "TaskDesignator",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    customer_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "CustomerIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(CTR|CTR-)([0-9])+",
        },
    )
    farm_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "FarmIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(FRM|FRM-)([0-9])+",
        },
    )
    partfield_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "PartfieldIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(PFD|PFD-)([0-9])+",
        },
    )
    responsible_worker_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "ResponsibleWorkerIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(WKR|WKR-)([0-9])+",
        },
    )
    status: None | TaskStatus = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "TaskStatus",
            "type": "Attribute",
            "required": True,
        },
    )
    default_treatment_zone_code: None | int = field(
        default=None,
        metadata={
            "name": "H",
            "full_name": "DefaultTreatmentZoneCode",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
    position_lost_treatment_zone_code: None | int = field(
        default=None,
        metadata={
            "name": "I",
            "full_name": "PositionLostTreatmentZoneCode",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
    out_of_field_treatment_zone_code: None | int = field(
        default=None,
        metadata={
            "name": "J",
            "full_name": "OutOfFieldTreatmentZoneCode",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 254,
        },
    )
