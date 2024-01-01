import re
from ScrapingTools.OutsourceTools.UrlsHandler import UrlsHandler
from urllib.parse import urlparse, urlunparse

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

            url_parts = url.split("/")
            jobs_index = url_parts.index("jobs")
            company = url_parts[jobs_index + 1]
            company = company.replace("-", "")

            if name != company:
                return False

        except Exception as e:
            print(e)
            return False
        return True


    def clear_url(self, url):
        parsed_url = urlparse(url)
        path_segments = parsed_url.path.split('/')
        base_path = '/'.join(path_segments[:-2])
        base_url = urlunparse((parsed_url.scheme, parsed_url.netloc, base_path, '', '', ''))
        return base_url

