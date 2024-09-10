from dataclasses import dataclass, field


@dataclass
class ProcessDataVariable:
    """
    ProcessDataVariable.

    :ivar process_data_variables: ProcessDataVariable
    :ivar process_data_ddi: A, (required)
    :ivar process_data_value: B, (required)
    :ivar product_id_ref: C
    :ivar device_element_id_ref: D
    :ivar value_presentation_id_ref: E
    """

    class Meta:
        name = "PDV"

    process_data_variables: list["ProcessDataVariable"] = field(
        default_factory=list,
        metadata={
            "name": "PDV",
            "full_name": "ProcessDataVariable",
            "type": "Element",
        },
    )
    process_data_ddi: None | bytes = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "ProcessDataDDI",
            "type": "Attribute",
            "required": True,
            "length": 2,
            "format": "base16",
        },
    )
    process_data_value: None | int = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "ProcessDataValue",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )
    product_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "ProductIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(PDT|PDT-)([0-9])+",
        },
    )
    device_element_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "DeviceElementIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(DET|DET-)([0-9])+",
        },
    )
    value_presentation_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "ValuePresentationIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(VPN|VPN-)([0-9])+",
        },
    )
