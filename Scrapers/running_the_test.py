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


directory_path = r'C:\Users\user\Documents\תכנות\Frashboard\job_scraping_demo\Scrapers\CompanyScrapers'
# run_pytest_on_files(directory_path)
# is_valid_file_name(directory_path)
