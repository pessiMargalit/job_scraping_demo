from googlesearch import search
import pandas as pd
import time


class UrlSearcher:
    @staticmethod
    def get_first_google_result(company_name, query):
        try:
            search_results = search(f'${company_name} {query}', num=1, stop=1, pause=2)  # Add a pause of 2 seconds
            first_result_url = next(search_results)
            return first_result_url

        except StopIteration:
            print("No search results found.")
            return None
        except Exception:
            print("Blocked by NetFree")
            return None

    @staticmethod
    def update_excel_urls(input_file, output_file):
        # Read the Excel file
        df = pd.read_excel(input_file, engine='openpyxl')

        # Create a new column for the URLs
        df['URL'] = df['Company Name'].apply(UrlSearcher.get_first_google_result, args='career')
        # Retry for timed-out queries
        retries = 3
        for i in range(retries):
            try:
                # Save the updated DataFrame to a new Excel file
                df.to_excel(output_file, index=False, engine='openpyxl')
                print("File updated successfully.")
                break
            except TimeoutError:
                print(f"TimeoutError: Retry {i + 1}/{retries}. Waiting for 5 seconds.")
                time.sleep(5)
                continue
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")
                break

# Replace 'input_file.xlsx' and 'output_file.xlsx' with your actual file names
# UrlSearcher.update_excel_urls('500 companies.xlsx', 'new career.xlsx')
