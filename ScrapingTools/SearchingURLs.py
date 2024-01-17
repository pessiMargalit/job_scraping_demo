from googlesearch import search
import pandas as pd
import time


def get_first_google_result(query):
    try:
        search_results = search(f'${query} career', num=1, stop=1, pause=2)  # Add a pause of 2 seconds
        first_result_url = next(search_results)
        print(query, ": ", first_result_url)
        return first_result_url

    except StopIteration:
        print("No search results found.")
        return None
    except Exception:
        print("Blocked by NetFree")
        return None


# Example usage:
# search_query = "Intel"
# first_result = get_first_google_result(search_query)
#
# if first_result:
#     print(f"The first result for '{search_query}' is: {first_result}")

def update_excel_urls(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file, engine='openpyxl')

    # Create a new column for the URLs
    df['URL'] = df['Company Name'].apply(get_first_google_result)
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
update_excel_urls('500 companies.xlsx', 'new career.xlsx')
