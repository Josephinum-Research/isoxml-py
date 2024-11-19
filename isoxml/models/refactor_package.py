import os
from refactor_helper import _extract_class_name, camel_to_snake


def search_and_replace_in_files(directory, search_string, replace_string):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Process only .txt files
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)

            # Read the contents of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Replace the search_string with replace_string
            new_content = content.replace(search_string, replace_string)

            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Processed {filename}")


def refactor_classes(package_path):
    for file in os.listdir(package_path):
        if not file.endswith(".py"):
            continue
        with open(package_path + '/' + file, 'r') as module_file:
            code = module_file.read()
        class_name = _extract_class_name(code)
        for old_name, new_name in class_name.items():
            search_and_replace_in_files(package_path, old_name, new_name)
            old_import = file.split('.')[0]
            new_import = camel_to_snake(new_name)
            search_and_replace_in_files(package_path, '.' + old_import + ' ', '.' + new_import + ' ')
            new_module = file.replace(old_import, new_import)
            os.rename(package_path + '/' + file, package_path + '/' + new_module)


if __name__ == '__main__':
    package_path = './base/v4'
    refactor_classes(package_path)
