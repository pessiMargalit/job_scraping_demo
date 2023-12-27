import os
import re
import subprocess
from os.path import dirname
from pathlib import Path


class ComeetCompany:
    def __init__(self, name, url=None):
        self.name = name
        self.url = url

    @staticmethod
    def transform_string(input_string):
        # Replace special characters with spaces
        cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', ' ', input_string)
        capitalized_string = cleaned_string.title()
        final_string = ''.join(capitalized_string.split())
        return final_string

    def generate_scraper(self, directory_path=None):
        """
        This function generate a comeet scraper using ComeetScraper class
        """
        if not directory_path:
            root_dir = os.path.dirname(dirname(dirname(os.path.abspath(__file__))))
            directory_path = root_dir + r"\Scrapers\CompanyScrapers\ComeetScrapers"
        name = self.transform_string(self.name) + "Scraper"
        code = \
            f"""
from Scrapers.Tools.ComeetScraper import ComeetScraper

class {name}(ComeetScraper):
    url = "{self.url}"
    name = "{self.name}"
    
    def scrape(self):
        super().scrape()
        
"""
        try:
            # Ensure the directory exists
            os.makedirs(directory_path, exist_ok=True)
            file_path = os.path.join(directory_path, name + ".py")
            with open(file_path, 'w') as file:
                file.write(code)

            print(f"Python file created successfully: {file_path}")
            return file_path
        except Exception as e:
            print(f"Error creating Python file: {e}")
            return None

    def create_branch(self, branch_name):
        """
        This function create a new branch using for the new scraper
        """
        if not branch_name:
            branch_name = self.name.replace(" ", "-").lower()
        try:
            # Create a new branch
            subprocess.run(["git", "checkout", "-b", branch_name], check=True)

            print(f"Branch '{branch_name}' created and checked out successfully.")
            return branch_name
        except subprocess.CalledProcessError as e:
            print(f"Error creating branch: {e}")

    @staticmethod
    def checkout_previous_branch():
        try:
            # Switch back to the previous branch
            subprocess.run(["git", "checkout", "-"], check=True)

            print("Switched back to the previous branch.")
        except subprocess.CalledProcessError as e:
            print(f"Error switching back to the previous branch: {e}")

    def add_commit_push(self, file_path, branch_name, commit_message=None):
        if not commit_message:
            commit_message = f"{self.name} scraper is ready!"
        try:
            subprocess.run(["git", "add", file_path], check=True)

            subprocess.run(["git", "commit", "-m", commit_message], check=True)

            subprocess.run(["git", "push", "--set-upstream", "origin", branch_name], check=True)

            print("Changes added, committed, and pushed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

# Flow:
# curve = ComeetCompany('Curve', "https.....")
# curve.create_branch()
# curve.generate_scraper()
# curve.commit_and_push()

