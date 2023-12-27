import os
import re
import subprocess
from os.path import dirname

from ScrapingTools.OutsourceTools.OutsourceCompany import OutsourceCompany


class ComeetCompany(OutsourceCompany):
    code_template = \
        """
from ScrapingTools.OutsourceTools.Comeet.BaseScraper import ComeetScraper


class {class_name}Scraper(ComeetScraper):
    url = "{url}"
    name = "{name}"

    def scrape(self):
        super().scrape()

    """

    def __init__(self, name, url=None):
        super().__init__(name, "comeet", url)

    def generate_scraper(self, directory_path=None):
        """
        This function generate a comeet scraper using ComeetScraper class
        """
        if not directory_path:
            root_dir = os.path.dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
            directory_path = root_dir + r"\Scrapers\CompanyScrapers\ComeetScrapers"
        name = self.transform_string(self.name)

        try:
            # Ensure the directory exists
            os.makedirs(directory_path, exist_ok=True)
            file_path = os.path.join(directory_path, name + "Scraper.py")
            with open(file_path, 'w') as file:
                code = self.code_template.format(class_name=self.transform_string(name), name=self.name, url=self.url)
                file.write(code)

            print(f"Python file created successfully: {file_path}")
            return file_path
        except Exception as e:
            print(f"Error creating Python file: {e}")
            return None

