import ast
import re
import subprocess

import os
import glob


def run_pytest_on_files(directory):
    # List all Python files in the directory, excluding __init__.py
    filenames = [filename for filename in os.listdir(directory)
                 if filename.endswith('.py') and '__init__' not in filename]

    # Construct the pytest command
    command = f"pytest --companies {','.join(filenames)}"
    print(command)
    # Execute the command in the specified directory
    result = subprocess.run(args=command, shell=True, cwd=directory, capture_output=True, text=True)

    # Print the result (stdout and stderr)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    print("Return Code:", result.returncode)


def is_valid_file_name(path):
    """
    prints the wrong file names
    """
    # Loop through all .py files in the specified directory
    for file_path in glob.glob(os.path.join(directory_path, '*.py')):
        # Extract the file name from the path
        file_name = os.path.basename(file_path)

        # Check if 'init' is not in the file name and 'Scraper' is not in the file name
        if 'init' not in file_name.lower() and 'Scraper' not in file_name:
            print(file_name)
            # Construct new file name by adding 'Scraper' to the original name
            # new_file_name = file_name.strip(".py")
            # new_file_name += 'Scraper.py'
            # new_file_path = os.path.join(directory_path, new_file_name)
            # os.rename(file_path, new_file_path)
            # print(f'Renamed "{file_name}" to "{new_file_name}"')


def get_python_classes(file_path):
    """Extract class names from a Python file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        node = ast.parse(file.read(), filename=file_path)
    return [n.name for n in ast.walk(node) if isinstance(n, ast.ClassDef)]

def camel_to_snake(name):
    """Convert CamelCase to snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def check_class_names(directory_path):
    """Check if class names match their file names (converted to snake_case)."""
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                class_names = get_python_classes(file_path)
                file_name_without_extension = os.path.splitext(file)[0]
                for class_name in class_names:
                    if class_name != file_name_without_extension:
                        print(f'File "{file_name_without_extension}" contains a class "{class_name}" that does not match the file name.')


directory_path = r'C:\Users\user\Documents\תכנות\Frashboard\job_scraping_demo\Scrapers\CompanyScrapers'
check_class_names(directory_path)
# run_pytest_on_files(directory_path)
# is_valid_file_name(directory_path)
