import json
import requests
import re

url = "https://www.isobus.net/isobus/exports/completeTXT"
response = requests.get(url)

if response.status_code == 200:
    with open("complete_data.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Datei erfolgreich heruntergeladen und gespeichert.")
else:
    print(f"Fehler beim Herunterladen der Datei: Status-Code {response.status_code}")

with open("complete_data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

dd_entities = {}
current_entity = {}


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
        name_cleaned = entity_match.group(2).replace("Â³", "³").replace("Â²", "²")
        current_entity = {
            "DDI": int(entity_match.group(1)),
            "name": name_cleaned,
            "unit": "",
            "bitResolution": 1.0,
        }
        continue


    unit_match = re.match(r"Unit: (.+) - (.+)", line)
    if unit_match:
        unit_cleaned = unit_match.group(1).replace("Â³", "³").replace("Â²", "²")
        current_entity["unit"] = unit_cleaned if unit_cleaned != "not defined" else ""
        continue

    resolution_match = re.match(r"Resolution: (.+)", line)
    if resolution_match:
        try:
            current_entity["bitResolution"] = float(resolution_match.group(1).replace(",", "."))
        except ValueError:
            pass

if current_entity:
    dd_entities[current_entity["DDI"]] = current_entity

with open("ddi_entities.json", "w", encoding="utf-8") as json_file:
    json.dump(dd_entities, json_file, indent=4, ensure_ascii=False)

print("Datei 'dd_entities.json' wurde erfolgreich gespeichert!")