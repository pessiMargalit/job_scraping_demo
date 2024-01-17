import concurrent.futures
import time
from urllib.error import HTTPError
from googlesearch import search
import pandas as pd


class UrlsHandler:
    @staticmethod
    def get_first_google_result(company_name):
        attempt_count = 0
        max_attempts = 2
        pause_duration = 3  # Increase the pause duration

        while attempt_count < max_attempts:
            try:
                search_results = search(f'{company_name} דרושים ', num=3, stop=3, pause=pause_duration)
                first_result_url = next(search_results)
                for result_url in search_results:
                    if not UrlsHandler.check_url(result_url):
                        print(company_name, ": ", result_url)
                        return result_url
                print(company_name, ": ", first_result_url)
                return first_result_url

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

    @staticmethod
    def check_url(url):
        guidestar_pattern = 'https://www.guidestar.org.il/organization/'
        return url.startswith(guidestar_pattern)

    @staticmethod
    def update_excel_urls(file_path, rows_to_process=200):
        df = pd.read_excel(file_path, engine='openpyxl', nrows=rows_to_process)

        # Use ThreadPoolExecutor to run get_first_google_result with multiple threads
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            urls = list(executor.map(UrlsHandler.get_first_google_result, df['Company Name']))

        df['URL'] = urls

        retries = 2
        for i in range(retries):
            try:
                df.to_excel(file_path, index=False, engine='openpyxl')
                print("File updated successfully.")
                break
            except TimeoutError:
                print(f"TimeoutError: Retry {i + 1}/{retries}. Waiting for 5 seconds.")
                time.sleep(5)
                continue
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")
                break


UrlsHandler.update_excel_urls('../Files/20k_companies.xlsx')
