from dataclasses import dataclass, field

from isoxml.models.base.v3.coded_comment import CodedComment
from isoxml.models.base.v3.coded_comment_group import CodedCommentGroup
from isoxml.models.base.v3.colour_legend import ColourLegend
from isoxml.models.base.v3.crop_type import CropType
from isoxml.models.base.v3.cultural_practice import CulturalPractice
from isoxml.models.base.v3.customer import Customer
from isoxml.models.base.v3.device import Device
from isoxml.models.base.v3.farm import Farm
from isoxml.models.base.v3.operation_technique import OperationTechnique
from isoxml.models.base.v3.partfield import Partfield
from isoxml.models.base.v3.product import Product
from isoxml.models.base.v3.product_group import ProductGroup
from isoxml.models.base.v3.task import Task
from isoxml.models.base.v3.value_presentation import ValuePresentation
from isoxml.models.base.v3.worker import Worker


@dataclass
class ExternalFileContents:
    """
    ExternalFileContents.

    :ivar coded_comments: CCT
    :ivar coded_comment_groups: CCG
    :ivar colour_legends: CLD
    :ivar crop_types: CTP
    :ivar cultural_practices: CPC
    :ivar customers: CTR
    :ivar devices: DVC
    :ivar farms: FRM
    :ivar operation_techniques: OTO
    :ivar partfields: PFD
    :ivar products: PDT
    :ivar product_groups: PGP
    :ivar tasks: TSK
    :ivar value_presentations: VPN
    :ivar workers: WKR
    """

    class Meta:
        name = "XFC"

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
