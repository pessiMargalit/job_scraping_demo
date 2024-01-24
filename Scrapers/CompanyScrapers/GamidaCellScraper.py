
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class GamidacellScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/gamidacell"
    name = 'Gamida Cell'

    def scrape(self):
        super().scrape()

