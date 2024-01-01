
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class BuymeScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/buyme/B2.008"
    name = "Buyme"

    def scrape(self):
        super().scrape()

    