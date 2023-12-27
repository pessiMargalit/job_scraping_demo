from googlesearch import search
import pandas as pd
from pathlib import Path


class UrlsHandler:
    def __init__(self, name):
        self.name = name

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

    def get_google_result(self, company):
        try:
            search_results = search(f'{self.name} {company} career', num=5, stop=1, pause=2)  # Add a pause of 2 seconds
            for result_url in next(search_results):
                if self.check_url(result_url):
                    return result_url
            return None
        except StopIteration:
            print("No search results found.")
            return None
        except Exception as e:
            print(e)
            return None

    def check_url(self, name, url):
        pass

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

    def create_new_branch(self, name, url):
        pass

    def scrape_with_dict(self, comp_dict):
        pass
