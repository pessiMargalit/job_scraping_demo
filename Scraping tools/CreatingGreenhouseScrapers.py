import pandas as pd
import os

# Read the Excel file into a DataFrame
excel_file_path = '../../../Careers files/greenhouse.xlsx'
df = pd.read_excel(excel_file_path)

# Define the template for the scraper code
template = """
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class {scraper_name}(GreenhouseScraper):
    official_url = "{official_url}"
    url = "{url}"
    name = '{company_name}'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


{scraper_name}().check_self()
"""

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    company_name = row['Company Name']
    link_to_official_website = row['Link To Website']
    link_to_website = row['Link To Greenhouse Website']
    # Create a Python file name based on the company name
    scraper_name = f"{company_name.replace(' ', '')}Scraper"
    file_name = os.path.join("../Scrapers/CompanyScrapers/GreenhouseScrapers", f"{scraper_name}.py")

    # Write the scraper code to the file
    with open(file_name, 'w') as file:
        file.write(template.format(scraper_name=scraper_name, official_url=link_to_official_website, url=link_to_website, company_name=company_name))
