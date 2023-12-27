import re

from googlesearch import search
import pandas as pd
import time
from pathlib import Path
from enum import Enum
import openpyxl

from Scrapers.Tools.ComeetCompany import ComeetCompany


class ComeetURLsHandler(UrlsHandler):
    allowed_extensions = {'csv': ".csv", 'excel': ".xlsx"}

    def initialize_company_dict(self, companies):
        if isinstance(companies, list):
            return {comp: "" for comp in companies}
        if isinstance(companies, str):
            result_dict = dict()
            file = Path(companies)
            if file.exists() and file.is_file and file.suffix in self.allowed_extensions.values():
                df = pd.read_excel(companies) if companies.endswith('.xlsx') else pd.read_csv(companies)
            for index, row in df.iterrows():
                name = row.iloc[0]  # Assuming the name is in the first column
                value = row.iloc[1] if len(row) > 1 else ''
                result_dict[name] = value
            return result_dict

    def get_first_google_result(self, query):
        # TODO: Find 5 first results and return the most accurate result
        try:
            search_results = search(f'comeet {query} career', num=1, stop=1, pause=2)  # Add a pause of 2 seconds
            first_result_url = next(search_results)
            print(query, ": ", first_result_url)
            return first_result_url

        except StopIteration:
            print("No search results found.")
            return None
        except Exception as e:
            print(e)
            return None

    def check_url(self, name, url):
        """
        This function check the URL if it is use comeet
        """
        try:
            comeet_prefix = "https://www.comeet.com/jobs/"
            if comeet_prefix not in url:
                return False
            # TODO - try to translate company name into english
            pattern = re.compile(r'^[a-zA-Z0-9!@#$%^&*()-_+=\[\]{};:\'",.<>?/`~\s]+$')
            if not bool(pattern.match(name)):
                return False
                # raise Exception("Error: Company name should be only English")

            # Checking if the company name is in the URL
            # TODO: Remove "Ltd" suffix and special chars

            name = name.lower().replace(" ", "")
            sub_url = url[len(comeet_prefix):]
            sub_url = sub_url.replace("-", "")
            if name not in sub_url:
                return False
        except Exception as e:
            print(e)
            return False
        return True

    def update_existing_urls(self, output_file_path, companies_dict):
        try:
            # Convert the dictionary to a DataFrame
            df = pd.DataFrame(list(companies_dict.items()), columns=['Company', 'URL'])
            # Write the DataFrame to the specified file path
            if output_file_path.endswith(self.allowed_extensions['csv']):
                df.to_csv(output_file_path, index=False)
            elif output_file_path.endswith(self.allowed_extensions['excel']):
                df.to_excel(output_file_path, index=False, engine='openpyxl')
            else:
                print("Unsupported file format. Please provide a CSV or Excel file.")
            print(f"Data successfully written to {output_file_path}")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def create_new_comeet_branch(self, name, url):
        cc = ComeetCompany(name, url)
        branch_name = cc.create_branch(branch_name=f"shoshanas/{name.lower()}")
        file_path = cc.generate_scraper()
        cc.add_commit_push(file_path, branch_name)
        cc.checkout_previous_branch()

    def scrape_with_dict(self, comp_dict):
        for name, url in comp_dict.items():
            self.create_new_comeet_branch(name, url)


def main():
    cuh = ComeetURLsHandler()
    companies = input("Please insert a route to companies list")
    # You can also insert an array with companies names
    comp_dict = cuh.initialize_company_dict(companies)
    copied_comp_dict = comp_dict.copy()
    for comp in copied_comp_dict.keys():
        url = cuh.get_first_google_result(comp)
        # TODO: Fix URLs like "https://www.comeet.com/jobs/surgimate/B7.00D/vp-of-customers/6B.A37"
        #  to be more general, like: "https://www.comeet.com/jobs/surgimate/B7.00D"
        if cuh.check_url(name=comp, url=url):
            comp_dict[comp] = url
        else:
            del comp_dict[comp]
        output_file = input("Please insert a route to companies list")
        cuh.update_existing_urls(output_file_path=output_file, companies_dict=comp_dict)


if __name__ == "__main__":
    main()
