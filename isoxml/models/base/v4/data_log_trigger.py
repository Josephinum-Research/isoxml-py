from dataclasses import dataclass, field


@dataclass
class DataLogTrigger:
    """
    DataLogTrigger.

    :ivar data_log_ddi: A, (required)
    :ivar data_log_method: B, (required)
    :ivar data_log_distance_interval: C
    :ivar data_log_time_interval: D
    :ivar data_log_threshold_minimum: E
    :ivar data_log_threshold_maximum: F
    :ivar data_log_threshold_change: G
    :ivar device_element_id_ref: H
    :ivar value_presentation_id_ref: I
    :ivar data_log_pgn: J
    :ivar data_log_pgn_start_bit: K
    :ivar data_log_pgn_stop_bit: L
    """

    class Meta:
        name = "DLT"

    data_log_ddi: None | bytes = field(
        default=None,
        metadata={
            "name": "A",
            "full_name": "DataLogDDI",
            "type": "Attribute",
            "required": True,
            "length": 2,
            "format": "base16",
        },
    )
    data_log_method: None | int = field(
        default=None,
        metadata={
            "name": "B",
            "full_name": "DataLogMethod",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 31,
        },
    )
    data_log_distance_interval: None | int = field(
        default=None,
        metadata={
            "name": "C",
            "full_name": "DataLogDistanceInterval",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 1000000,
        },
    )
    data_log_time_interval: None | int = field(
        default=None,
        metadata={
            "name": "D",
            "full_name": "DataLogTimeInterval",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 60000,
        },
    )
    data_log_threshold_minimum: None | int = field(
        default=None,
        metadata={
            "name": "E",
            "full_name": "DataLogThresholdMinimum",
            "type": "Attribute",
            "min_inclusive": -2147483647,
            "max_inclusive": 2147483647,
        },
    )
    data_log_threshold_maximum: None | int = field(
        default=None,
        metadata={
            "name": "F",
            "full_name": "DataLogThresholdMaximum",
            "type": "Attribute",
            "min_inclusive": -2147483647,
            "max_inclusive": 2147483647,
        },
    )
    data_log_threshold_change: None | int = field(
        default=None,
        metadata={
            "name": "G",
            "full_name": "DataLogThresholdChange",
            "type": "Attribute",
            "min_inclusive": -2147483647,
            "max_inclusive": 2147483647,
        },
    )
    device_element_id_ref: None | str = field(
        default=None,
        metadata={
            "name": "H",
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
            "name": "I",
            "full_name": "ValuePresentationIdRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 14,
            "pattern": r"(VPN|VPN-)([0-9])+",
        },
    )
    data_log_pgn: None | int = field(
        default=None,
        metadata={
            "name": "J",
            "full_name": "DataLogPGN",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 262143,
        },
    )
    data_log_pgn_start_bit: None | int = field(
        default=None,
        metadata={
            "name": "K",
            "full_name": "DataLogPGNStartBit",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 63,
        },
    )
    data_log_pgn_stop_bit: None | int = field(
        default=None,
        metadata={
            "name": "L",
            "full_name": "DataLogPGNStopBit",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 63,
        },
    )
