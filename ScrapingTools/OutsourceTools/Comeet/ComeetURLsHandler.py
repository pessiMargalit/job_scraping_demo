import re
from ScrapingTools.OutsourceTools.UrlsHandler import UrlsHandler


class ComeetURLsHandler(UrlsHandler):
    outsource_name = "comeet"

    def __init__(self):
        super().__init__(self.outsource_name)

    def get_google_result(self, company):
        return super().get_google_result(company)

    def check_url(self, name, url):
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
            name = name.lower().replace(" ", "")
            sub_url = url[len(comeet_prefix):]
            sub_url = sub_url.replace("-", "")
            if name not in sub_url:
                return False
        except Exception as e:
            print(e)
            return False
        return True


