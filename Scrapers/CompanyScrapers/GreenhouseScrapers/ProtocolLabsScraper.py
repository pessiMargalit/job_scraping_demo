
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class ProtocolLabsScraper(GreenhouseScraper):
    official_url = "https://protocol.ai/join/"
    url = "https://boards.greenhouse.io/protocollabs/jobs/4945211004"
    name = 'Protocol Labs'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


ProtocolLabsScraper().check_self()
