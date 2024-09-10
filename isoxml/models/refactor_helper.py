import argparse
import re
from decimal import Decimal

def _parse_docstring(docstring):
    name_map = {}
    # Find all :cvar VALUE_ lines and extract the first word after the colon
    pattern = r"\:ivar\s(\w+)\:\s(\w+)"
    matches = re.findall(pattern, docstring)
    for match in matches:
        var_name, doc_name = match

        name_map[var_name] = doc_name
    return name_map


def _extract_class_name(code):
    pattern = r"\@dataclass\nclass\s(\w+):\n\s+\"{3}\n\s+(\w+)\."
    matches = re.findall(pattern, code)
    class_map = {}
    for name, full_name in matches:
        class_map[name] = full_name
    return class_map


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def _extract_enum_replacements(name_map):
    replacements = {}
    for old_value, new_name in name_map.items():

        if new_name == "":
            continue
        new_name = camel_to_snake(new_name)
        new_name = new_name.replace(" ", "_")
        new_name = ' ' + new_name + ': '
        replacements[f' {old_value}: '] = new_name
    return replacements


def _fix_field_nameing(name_map: dict, src: str) -> str:
    replacements = _extract_enum_replacements(name_map)

    replacements_aesc = {}
    for k in sorted(replacements, key=len, reverse=False):
        replacements_aesc[k] = replacements[k]

    new_code = src
    for old, new in replacements_aesc.items():
        if new_code.count(old) == 2:
            new_code = new_code.replace(old, new)
        else:
            raise Exception('unsafe replacement')
    print(new_code)
    return new_code


def add_full_name(name_map: dict, src: str) -> str:
    new_code = src
    for var_name, full_name in name_map.items():
        metadata_field = f'"name": "{var_name.upper()}",\n'
        subst = f'{metadata_field}            "full_name": "{full_name}",\n'
        new_code = new_code.replace(metadata_field, subst)
    return new_code


def _fix_verbose_names(class_name, src: str) -> str:
    class_var_prefix = f'{camel_to_snake(class_name)}_'
    pattern = re.escape(class_var_prefix) + r"(\w{2,})\:\s"
    matches = re.findall(pattern, src)
    new_code = src
    for short_name in matches:
        new_code = new_code.replace(f"{class_var_prefix}{short_name}: ", f"{short_name}: ")
    return new_code


def _update_docstring(src: str) -> str:
    pattern = r"(\w+)\:\s[\w\s\|\[\]]+\=[\s\w\(\=\,]+metadata\=(\{.{,320}\})\,"
    matches = re.findall(pattern, src, re.DOTALL)
    new_code = src
    for var_name, metadata_str in matches:
        metadata: dict = eval(metadata_str)
        assert isinstance(metadata, dict)
        new_doc = f":ivar {var_name}: {metadata['name']}"
        if 'required' in metadata and metadata['required']:
            new_doc = new_doc + ', (required)'
        pattern_old_doc = r"\s{4}(:ivar\s" + re.escape(var_name) + r"\:.*)"
        doc_matches = re.findall(pattern_old_doc, new_code)
        assert len(doc_matches) == 1
        new_code = new_code.replace(doc_matches[0], new_doc)

    return new_code

def all():
    parser = argparse.ArgumentParser(description="Fix Enums created via xsdata")

    # Add arguments
    parser.add_argument("model_file", type=str, help="the python file to fix")

    # Parse the arguments
    args = parser.parse_args()

    with open(args.model_file, "r") as f:
        old_code = f.read()

    doc_string = old_code.split('"""')[1]
    name_map = _parse_docstring(doc_string)

    new_code = add_full_name(name_map, old_code)
    new_code = _fix_field_nameing(name_map, new_code)
    class_map = _extract_class_name(new_code)
    for _, v in class_map.items():
        new_code = _fix_verbose_names(v, new_code)

    new_code = _update_docstring(new_code)
    print(new_code)
    with open(args.model_file, "w") as f:
        f.write(new_code)


def doc():
    parser = argparse.ArgumentParser(description="Fix Enums created via xsdata")

    # Add arguments
    parser.add_argument("model_file", type=str, help="the python file to fix")

    # Parse the arguments
    args = parser.parse_args()

    with open(args.model_file, "r") as f:
        old_code = f.read()
    new_code = _update_docstring(old_code)
    print(new_code)
    with open(args.model_file, "w") as f:
        f.write(new_code)

if __name__ == '__main__':
    doc()
