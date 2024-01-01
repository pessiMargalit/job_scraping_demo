
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class ArbeScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/arbe/C6.001"
    name = "Arbe"

    def scrape(self):
        super().scrape()

    