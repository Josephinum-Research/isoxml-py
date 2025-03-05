import json
import requests
import re

if __name__ == '__main__':
    url = "https://www.isobus.net/isobus/exports/completeTXT"
    response = requests.get(url)
    response.raise_for_status()

    response.encoding = response.apparent_encoding
    lines = response.text.splitlines()

    dd_entities = {}
    current_entity = None

    start_parsing = False

    for line in lines:
        line = line.strip()

        if line.startswith("DD Entity:"):
            start_parsing = True

        if not start_parsing or not line:
            continue

        entity_match = re.match(r"DD Entity: (\d+) (.+)", line)
        if entity_match:
            if current_entity:
                dd_entities[current_entity["DDI"]] = current_entity

            ddi_number = int(entity_match.group(1))
            name = entity_match.group(2)

            current_entity = {
                "DDI": ddi_number,
                "name": name,
            }
            continue

        unit_match = re.match(r"Unit: (.+) - (.+)", line)
        if unit_match:
            unit = unit_match.group(1)
            if unit != "not defined":
                current_entity["unit"] = unit
            continue

        resolution_match = re.match(r"Resolution: (.+)", line)
        if resolution_match:
            current_entity["bitResolution"] = float(resolution_match.group(1).replace(",", "."))

    if current_entity:
        dd_entities[current_entity["DDI"]] = current_entity

    with open("ddi_entities.json", "w", encoding="utf-8") as json_file:
        json.dump(dd_entities, json_file, indent=4, ensure_ascii=False)

    print("File 'dd_entities.json' saved!")