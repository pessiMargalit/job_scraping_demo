import re

from googlesearch import search

from ScrapingTools.OutsourceTools.UrlsHandler import UrlsHandler


class GreenhouseURLsHandler(UrlsHandler):
    outsource_name = "greenhouse"

    def __init__(self):
        super().__init__(self.outsource_name)

    def get_google_result(self, company_name):
        return super().get_google_result(company_name)

    def check_url(self, url, name):
        """
        This function check the URL if it is use greenhouse
        """
        try:
            greenhouse_pattern = re.compile(r'https://boards(?:\.[a-zA-Z]+)?\.greenhouse\.io')
            if not greenhouse_pattern.search(url):
                return False
            # Checking if the company name is in the URL
            name = name.lower().replace(" ", "").replace(" Ltd", "")
            url = url.lower()
            sub_url = url.replace("-", "")
            if '.' in name and name not in sub_url:
                name = name.replace('.', '')
            if name not in sub_url:
                return False
        except Exception as e:
            print(e)
            return False
        return True

