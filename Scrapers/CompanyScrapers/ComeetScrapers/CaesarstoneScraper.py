
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class CaesarstoneScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/caesarstone/25.000"
    name = "caesarstone"

    def scrape(self):
        super().scrape()

    