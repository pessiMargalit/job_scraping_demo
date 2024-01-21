import os


def find_files_with_location(directory, search_string):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line.__contains__(search_string):
                            print(filename)
                            break
            except UnicodeDecodeError:
                print(f"Could not read {filename} due to encoding issue")


directory_path = r'C:\Users\user\Documents\תכנות\Frashboard\job_scraping_demo\Scrapers\CompanyScrapers'
search_string = 'location = \'Jerusalem\''

find_files_with_location(directory_path, search_string)
