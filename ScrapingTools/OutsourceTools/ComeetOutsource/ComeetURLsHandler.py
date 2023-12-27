import re
from googlesearch import search
import pandas as pd
from pathlib import Path

from ScrapingTools.OutsourceTools.ComeetOutsource.ComeetCompany import ComeetCompany
from ScrapingTools.OutsourceTools.UrlsHandler import UrlsHandler


class ComeetURLsHandler(UrlsHandler):
    name = "comeet"

    def get_google_result(self, company):
        super().get_google_result(company)

    def check_url(self, name, url):
        """
        This function check the URL if it is use comeet
        """
        try:
            comeet_prefix = "https://www.comeet.com/jobs/"
            if comeet_prefix not in url:
                return False
            # TODO - try to translate company name into english
            pattern = re.compile(r'^[a-zA-Z0-9!@#$%^&*()-_+=\[\]{};:\'",.<>?/`~\s]+$')
            if not bool(pattern.match(name)):
                return False
                # raise Exception("Error: Company name should be only English")

            # Checking if the company name is in the URL
            # TODO: Remove "Ltd" suffix and special chars

            name = name.lower().replace(" ", "")
            sub_url = url[len(comeet_prefix):]
            sub_url = sub_url.replace("-", "")
            if name not in sub_url:
                return False
        except Exception as e:
            print(e)
            return False
        return True

    def create_new_branch(self, name, url):
        cc = ComeetCompany(name, url)
        branch_name = cc.create_branch()
        file_path = cc.generate_scraper()
        cc.add_commit_push(file_path, branch_name)
        cc.checkout_previous_branch()

    def scrape_with_dict(self, comp_dict):
        for name, url in comp_dict.items():
            # self.create_new_branch(name, url)
            cc = ComeetCompany(name, url)
            file_path = cc.generate_scraper()


def main():
    cuh = ComeetURLsHandler()
    companies = input("Please insert a route to companies list")
    # You can also insert an array with companies names
    comp_dict = cuh.initialize_company_dict(companies)
    copied_comp_dict = comp_dict.copy()
    for comp in copied_comp_dict.keys():
        url = cuh.get_first_google_result(comp)
        # TODO: Fix URLs like "https://www.comeet.com/jobs/surgimate/B7.00D/vp-of-customers/6B.A37"
        #  to be more general, like: "https://www.comeet.com/jobs/surgimate/B7.00D"
        if cuh.check_url(name=comp, url=url):
            comp_dict[comp] = url
        else:
            del comp_dict[comp]
        output_file = input("Please insert a route to companies list")
        cuh.update_existing_urls(output_file_path=output_file, companies_dict=comp_dict)


if __name__ == "__main__":
    main()
