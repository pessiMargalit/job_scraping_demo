
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class GamidaCellScraper(GreenhouseScraper):
    url = "https://boards.greenhouse.io/gamidacell"
    name = 'Gamida Cell'

    def scrape(self):
        super().scrape()

