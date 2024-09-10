from dataclasses import dataclass, field
from enum import Enum

from isoxml.models.base.v4.attached_file import AttachedFile
from isoxml.models.base.v4.base_station import BaseStation
from isoxml.models.base.v4.coded_comment import CodedComment
from isoxml.models.base.v4.coded_comment_group import CodedCommentGroup
from isoxml.models.base.v4.colour_legend import ColourLegend
from isoxml.models.base.v4.crop_type import CropType
from isoxml.models.base.v4.cultural_practice import CulturalPractice
from isoxml.models.base.v4.customer import Customer
from isoxml.models.base.v4.device import Device
from isoxml.models.base.v4.external_file_reference import ExternalFileReference
from isoxml.models.base.v4.farm import Farm
from isoxml.models.base.v4.operation_technique import OperationTechnique
from isoxml.models.base.v4.partfield import Partfield
from isoxml.models.base.v4.product import Product
from isoxml.models.base.v4.product_group import ProductGroup
from isoxml.models.base.v4.task import Task
from isoxml.models.base.v4.task_controller_capabilities import TaskControllerCapabilities
from isoxml.models.base.v4.value_presentation import ValuePresentation
from isoxml.models.base.v4.worker import Worker


class Iso11783TaskDataDataTransferOrigin(Enum):
    FMIS = "1"
    MICS = "2"


class Iso11783TaskDataVersionMajor(Enum):
    VALUE_4 = "4"


class Iso11783TaskDataVersionMinor(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


@dataclass
class Iso11783TaskData:
    """
    ISO 11783 Task Data File.

    :ivar attached_files: AFE
    :ivar base_stations: BSN
    :ivar coded_comments: CCT
    :ivar coded_comment_groups: CCG
    :ivar colour_legends: CLD
    :ivar crop_types: CTP
    :ivar cultural_practices: CPC
    :ivar customers: CTR
    :ivar devices: DVC
    :ivar farms: FRM
    :ivar operation_techniques: OTQ
    :ivar partfields: PFD
    :ivar products: PDT
    :ivar product_groups: PGP
    :ivar tasks: TSK
    :ivar task_controller_capabilities: TCC
    :ivar value_presentations: VPN
    :ivar workers: WKR
    :ivar external_file_references: XFR
    :ivar version_major: Version Major, (default: 4)
    :ivar version_minor: Version Minor, (default: 3)
    :ivar management_software_manufacturer: ManagementSoftwareManufacturer, (required)
    :ivar management_software_version: ManagementSoftwareVersion, (required)
    :ivar task_controller_manufacturer: TaskControllerManufacturer
    :ivar task_controller_version: TaskControllerVersion
    :ivar data_transfer_origin: DataTransferOrigin, (required)
    :ivar lang:
    """

    class Meta:
        name = "ISO11783_TaskData"

    attached_files: list[AttachedFile] = field(
        default_factory=list,
        metadata={
            "name": "AFE",
            "type": "Element",
        },
    )
    base_stations: list[BaseStation] = field(
        default_factory=list,
        metadata={
            "name": "BSN",
            "type": "Element",
        },
    )
    coded_comments: list[CodedComment] = field(
        default_factory=list,
        metadata={
            "name": "CCT",
            "type": "Element",
        },
    )
    coded_comment_groups: list[CodedCommentGroup] = field(
        default_factory=list,
        metadata={
            "name": "CCG",
            "type": "Element",
        },
    )
    colour_legends: list[ColourLegend] = field(
        default_factory=list,
        metadata={
            "name": "CLD",
            "type": "Element",
        },
    )
    crop_types: list[CropType] = field(
        default_factory=list,
        metadata={
            "name": "CTP",
            "type": "Element",
        },
    )
    cultural_practices: list[CulturalPractice] = field(
        default_factory=list,
        metadata={
            "name": "CPC",
            "type": "Element",
        },
    )
    customers: list[Customer] = field(
        default_factory=list,
        metadata={
            "name": "CTR",
            "type": "Element",
        },
    )
    devices: list[Device] = field(
        default_factory=list,
        metadata={
            "name": "DVC",
            "type": "Element",
        },
    )
    farms: list[Farm] = field(
        default_factory=list,
        metadata={
            "name": "FRM",
            "type": "Element",
        },
    )
    operation_techniques: list[OperationTechnique] = field(
        default_factory=list,
        metadata={
            "name": "OTQ",
            "type": "Element",
        },
    )
    partfields: list[Partfield] = field(
        default_factory=list,
        metadata={
            "name": "PFD",
            "type": "Element",
        },
    )
    products: list[Product] = field(
        default_factory=list,
        metadata={
            "name": "PDT",
            "type": "Element",
        },
    )
    product_groups: list[ProductGroup] = field(
        default_factory=list,
        metadata={
            "name": "PGP",
            "type": "Element",
        },
    )
    tasks: list[Task] = field(
        default_factory=list,
        metadata={
            "name": "TSK",
            "type": "Element",
        },
    )
    task_controller_capabilities: list[TaskControllerCapabilities] = field(
        default_factory=list,
        metadata={
            "name": "TCC",
            "type": "Element",
        },
    )
    value_presentations: list[ValuePresentation] = field(
        default_factory=list,
        metadata={
            "name": "VPN",
            "type": "Element",
        },
    )
    workers: list[Worker] = field(
        default_factory=list,
        metadata={
            "name": "WKR",
            "type": "Element",
        },
    )
    external_file_references: list[ExternalFileReference] = field(
        default_factory=list,
        metadata={
            "name": "XFR",
            "type": "Element",
        },
    )
    version_major: Iso11783TaskDataVersionMajor = field(
        init=False,
        default=Iso11783TaskDataVersionMajor.VALUE_4,
        metadata={
            "name": "VersionMajor",
            "type": "Attribute",
            "required": True,
        },
    )
    version_minor: None | Iso11783TaskDataVersionMinor = field(
        default=Iso11783TaskDataVersionMinor.VALUE_3,
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
    data_transfer_origin: None | Iso11783TaskDataDataTransferOrigin = field(
        default=None,
        metadata={
            "name": "DataTransferOrigin",
            "type": "Attribute",
            "required": True,
        },
    )
    lang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 32,
        },
    )
