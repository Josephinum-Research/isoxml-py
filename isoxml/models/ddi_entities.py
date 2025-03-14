"""
see https://www.isobus.net/isobus/dDEntity
"""
import json
from dataclasses import dataclass
from importlib import resources

with resources.open_text("isoxml.data", "ddi_entities.json", encoding="utf-8") as file:
    _dd_entities = json.load(file)
_dd_entities = {int(k): v for k, v in _dd_entities.items()}


@dataclass
class DDEntity:
    ddi: int
    name: str
    unit: str | None
    bit_resolution: float

    def __bytes__(self):
        return self.ddi.to_bytes(length=2, byteorder='big')

    @staticmethod
    def from_id(ddi: int):
        ddi_dict = _dd_entities[ddi]
        return DDEntity(
            ddi=ddi_dict['DDI'],
            name=ddi_dict['name'],
            unit=getattr(ddi_dict, 'unit', None),
            bit_resolution=ddi_dict['bitResolution']
        )

    @staticmethod
    def from_bytes(ddi_bytes: bytes):
        return DDEntity.from_id(int.from_bytes(ddi_bytes, byteorder='big'))
