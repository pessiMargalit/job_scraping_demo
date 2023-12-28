import re
import time
from urllib.error import HTTPError

from googlesearch import search
import pandas as pd
from pathlib import Path


class UrlsHandler:
    def __init__(self, outsource_name):
        self.outsource_name = outsource_name

    allowed_extensions = {'csv': ".csv", 'excel': ".xlsx"}

    def initialize_company_dict(self, companies):
        if isinstance(companies, list):
            return {self.clear_company_name(comp): "" for comp in companies}
        if isinstance(companies, str):
            result_dict = dict()
            file = Path(companies)
            if file.exists() and file.is_file and file.suffix in self.allowed_extensions.values():
                df = pd.read_excel(companies) if companies.endswith('.xlsx') else pd.read_csv(companies)
                for index, row in df.iterrows():
                    name = row.iloc[0]  # Assuming the name is in the first column
                    name = self.clear_company_name(name)
                    value = row.iloc[1] if len(row) > 1 else ''
                    result_dict[name] = value
            return result_dict

    def get_google_result(self, company_name):
        attempt_count = 0
        max_attempts = 5
        pause_duration = 5  # Increase the pause duration

        while attempt_count < max_attempts:
            try:
                search_results = search(f'{self.outsource_name} {company_name} career', num=5, pause=pause_duration)
                for result_url in search_results:
                    if self.check_url(result_url, company_name):
                        return result_url
                return None

            except HTTPError as e:
                if e.code == 429:
                    print("Rate limit hit. Waiting to retry...")
                    time.sleep(pause_duration)  # Wait before retrying
                    pause_duration *= 2  # Exponential backoff
                    attempt_count += 1
                else:
                    print(e)
                    return None

            except StopIteration:
                print("No search results found.")
                return None

            except Exception as e:
                print(e)
                return None
        try:
            search_results = search(f'{self.outsource_name} {company_name} career', num=5, stop=5, pause=2)
            for result_url in search_results:
                if self.check_url(result_url, company_name):
                    return result_url
            search_results = search(f'{self.outsource_name} {company_name}', num=5, stop=5, pause=2)
            for result_url in search_results:
                if self.check_url(result_url, company_name):
                    return result_url
            return None
        except StopIteration:
            print("No search results found.")
            return None
        except Exception as e:
            print(e)
            return None
            # if attempt_count == max_attempts:
            #     print("Maximum attempts reached. Exiting.")
            #     return None

    def check_url(self, name, url):
        pass

    def update_existing_urls(self, output_file_path, companies_dict):
        try:
            # Convert the dictionary to a DataFrame
            df = pd.DataFrame(list(companies_dict.items()), columns=['Company', 'URL'])
            print(df)
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

    def perform_urls_handler_flow(self):
        companies = input("Please insert a route for companies list\n")
        # You can also insert an array with companies names
        comp_dict = self.initialize_company_dict(companies)
        copied_comp_dict = comp_dict.copy()
        for comp in copied_comp_dict.keys():
            url = self.get_google_result(comp)
            if url is None:
                del comp_dict[comp]
            else:
                comp_dict[comp] = url
        output_file = input("Please insert a route to companies list\n")
        self.update_existing_urls(output_file_path=output_file, companies_dict=comp_dict)
        return comp_dict

    @staticmethod
    def clear_company_name(company):
        #  Remove "Ltd" suffix and special chars
        # remove the (...)
        name = re.sub(r'\([^)]*\)', '', company)
        if 'Ltd.' in name:
            name = name.replace('Ltd.', '').rstrip()
        return name
