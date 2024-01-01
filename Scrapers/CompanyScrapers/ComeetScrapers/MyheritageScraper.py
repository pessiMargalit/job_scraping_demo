
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class MyheritageScraper(ComeetScraper):
    url = "https://careers.myheritage.com/"
    name = "MyHeritage"

    def scrape(self):
        super().scrape()

    