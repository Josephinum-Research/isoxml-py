from dataclasses import dataclass, field


@dataclass
class DataLogValue:
    """
    DataLogValue.

    :ivar process_data_ddi: A, (required)
    :ivar process_data_value: B, (required)
    :ivar device_element_id_ref: C, (required)
    :ivar data_log_pgn: D
    :ivar data_log_pgn_start_bit: E
    :ivar data_log_pgn_stop_bit: F
    """

    class Meta:
        name = "DLV"

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
    device_element_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "DeviceElementIdRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(DET|DET-)([0-9])+",
        },
    )
    data_log_pgn: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "DataLogPGN",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 262143,
        },
    )
    data_log_pgn_start_bit: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "DataLogPGNStartBit",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 63,
        },
    )
    data_log_pgn_stop_bit: None | int = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "DataLogPGNStopBit",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 63,
        },
    )
