import os
import subprocess


def run_pytest_on_files(directory):
    """
    This function iterates over all files in the specified directory.
    For each file, it runs the command 'pytest --companies <file_name>'
    and prints the filename along with whether the test passed or failed.
    """
    for filename in os.listdir(directory):
        if filename.endswith('.py') and not filename.__contains__('__init__'):
            # Construct the pytest command
            command = f"pytest --companies {filename}"
            # Run the command and capture the output and return code
            result = subprocess.run(command, shell=True, cwd=directory, capture_output=True, text=True)
            print(result)
            # Check if the pytest command was successful (return code 0)
            if result.returncode == 0:
                status = 'passed'
            else:
                status = 'failed'
            print(f"{filename}: {status}")


# Example usage
directory_path = r"C:\Users\user\Documents\תכנות\Frashboard\job_scraping_demo\Scrapers\CompanyScrapers"
run_pytest_on_files(directory_path)
