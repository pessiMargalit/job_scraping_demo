import re
from ScrapingTools.OutsourceTools.UrlsHandler import UrlsHandler


class GreenhouseURLsHandler(UrlsHandler):
    outsource_name = "greenhouse"

    def __init__(self):
        super().__init__(self.outsource_name)

    def get_google_result(self, company):
        super().get_google_result(company)

    def check_url(self, name, url):
        try:
            greenhouse_prefix = "https://boards.greenhouse.io/"
            if greenhouse_prefix not in url:
                return False
            # TODO - try to translate company name into english
            pattern = re.compile(r'^[a-zA-Z0-9!@#$%^&*()-_+=\[\]{};:\'",.<>?/`~\s]+$')
            if not bool(pattern.match(name)):
                return False
                # raise Exception("Error: Company name should be only English")

            # Checking if the company name is in the URL
            # TODO: Remove "Ltd" suffix and special chars

            name = name.lower().replace(" ", "")
            sub_url = url[len(greenhouse_prefix):]
            sub_url = sub_url.replace("-", "")
            if name not in sub_url:
                return False
        except Exception as e:
            print(e)
            return False
        return True



