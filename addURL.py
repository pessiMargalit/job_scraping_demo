import glob
import re

# Specify the directory containing the .py files
directory = r'C:\Users\User\Desktop\חני\freshboard new\job_scraping_demo\Scrapers\CompanyScrapers'

# Find all .py files in the directory
py_files = glob.glob(f'{directory}/*.py')
url_pattern = re.compile(r'url\s*=\s*[\'"](.*?)[\'"]')  # Regular expression to match 'url = "some_url"'
for file_path in py_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if 'url' is in the file
        url_match = url_pattern.search(content)
        if url_match:
            print(f"URL found in {file_path}: {url_match.group(1)}")
        else:
            print(f"'url' not found in {file_path}")
        # else:
        #     lines = content.splitlines()
        #     # Remove lines ending with "checkSelf()"
        #     lines = [line for line in lines if not line.rstrip().endswith('checkSelf()')]
        #
        #     with open(file_path, 'w', encoding='utf-8') as file:
        #         file.writelines(line + '\n' for line in lines)

    except UnicodeDecodeError:
        print(f"Error processing file: {file_path}")

print(f"Processed {len(py_files)} files.")
# import glob
#
# # Specify the directory containing the .py files
# directory = r'C:\Users\User\Desktop\חני\freshboard new\job_scraping_demo\Scrapers\CompanyScrapers'
#
# # Find all .py files in the directory
# py_files = glob.glob(f'{directory}/*.py')
#
# for file_path in py_files:
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()
#
#         # Check if 'url = 'https://www.' is in the file
#         if "https://www." not in content:
#             print(f"'url = 'https://www.'' not found in {file_path}")
#         else:
#             lines = content.splitlines()
#             # Remove lines ending with "checkSelf()"
#             lines = [line for line in lines if not line.rstrip().endswith('checkSelf()')]
#
#             with open(file_path, 'w', encoding='utf-8') as file:
#                 file.writelines(line + '\n' for line in lines)
#
#     except UnicodeDecodeError:
#         print(f"Error processing file: {file_path}")
#
# print(f"Processed {len(py_files)} files.")
