
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class ChronosphereScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/chronosphere"
    name = 'Chronosphere'

    def scrape(self):
        super().scrape()

