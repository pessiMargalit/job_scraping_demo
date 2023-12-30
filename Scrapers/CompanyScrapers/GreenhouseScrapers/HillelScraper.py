
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class HillelScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/hillel"
    name = 'Hillel'

    def scrape(self):
        super().scrape()

