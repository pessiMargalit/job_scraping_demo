# import pandas as pd
# import requests


# def find_specific_string(url, target_string):
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()  # Raise an exception for bad responses
#
#         if target_string in response.text:
#             return True
#         else:
#             return False
#     except:
#         return False
#
#
# # Example usage
# excel_file_path = '../../../Careers files/greenhouse.xlsx'
# df = pd.read_excel(excel_file_path)
#
# target_string = 'greenhouse.io'
# counter = 0
# companies_name = []
# # url = 'https://www.liveperson.com/company/careers/'
# for index, row in df.iterrows():
#     link = row['Link To Website']
#     # if str(link) != "nan" and ("linkedin" not in link and "indeed" not in link and "instagram" not in link):
#     result_tag = find_specific_string(link, target_string)
#     print(link)
#     if result_tag:
#         counter += 1
#         companies_name.append(df['Company Name'])
#         print(counter)
# print("counter: ", counter)
# print(companies_name)
import pandas as pd
import requests
from bs4 import BeautifulSoup


def check_for_string(url, search_string):
    try:
        # Fetch the HTML content of the web page
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad requests

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if the search string is present in the href or src attributes
        found = False
        for tag in soup.find_all(True):
            for attribute, value in tag.attrs.items():
                if isinstance(value, str) and search_string in value:
                    found = True
                    break
        if found:
            print(f'The string "{search_string}" was found in the href or src attributes on the page.')
        else:
            print(f'The string "{search_string}" was not found in the href or src attributes on the page.')

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# Replace 'https://example.com' with the actual URL you want to check
# excel_file_path = '../../../Careers files/greenhouse.xlsx'
# df = pd.read_excel(excel_file_path)
search_string = 'greenhous.io'
# counter = 0
# companies_name = []
# url = 'https://www.liveperson.com/company/careers/'
# for index, row in df.iterrows():
#     link = row['Link To Website']
# if str(link) != "nan" and ("linkedin" not in link and "indeed" not in link and "instagram" not in link):
check_for_string('https://www.axonius.com/company/careers/open-jobs', search_string)
# print(link)
# if result_tag:
#     counter += 1
#     companies_name.append(df['Company Name'])
#     print(counter)
# print("counter: ", counter)
# print(companies_name)
