
from ScrapingTools.OutsourceTools.Comeet.BaseScraper import ComeetScraper


class Pax8Scraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/pax8/52.008"
    name = "Pax8"

    def scrape(self):
        super().scrape()

    