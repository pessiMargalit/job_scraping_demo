import re
import subprocess


class OutsourceCompany:
    def __init__(self, name, branch_name, url=None):
        self.name = name
        self.url = url
        self.branch_name = branch_name

    @staticmethod
    def transform_string(input_string):
        # Replace special characters with spaces
        cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', ' ', input_string)
        capitalized_string = cleaned_string.title()
        final_string = ''.join(capitalized_string.split())
        return final_string

    def generate_scraper(self, directory_path=None):
        pass

    def create_branch(self, branch_name=None):
        """
        This function create a new branch using for the new scraper
        """
        if not branch_name:
            branch_name = self.branch_name
            # branch_name = self.name.replace(" ", "-").lower()
        try:
            # Create a new branch
            subprocess.run(["git", "checkout", "-b", branch_name], check=True)

            print(f"Branch '{branch_name}' created and checked out successfully.")
            return branch_name
        except subprocess.CalledProcessError as e:
            print(f"Error creating branch: {e}")

    @staticmethod
    def checkout_branch(name):
        try:
            # Switch back to the previous branch
            subprocess.run(["git", "checkout", name], check=True)

            print(f"Switched to the branch {name}.")
        except subprocess.CalledProcessError as e:
            print(f"Error switching to branch {name}: {e}")

    def checkout_previous_branch(self):
        self.checkout_branch("-")

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
