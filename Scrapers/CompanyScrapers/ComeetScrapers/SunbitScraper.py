
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class SunbitScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/sunbit/37.001"
    name = "sunbit"

    def scrape(self):
        super().scrape()

    