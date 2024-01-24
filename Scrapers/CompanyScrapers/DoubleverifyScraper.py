
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class DoubleverifyScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/doubleverify"
    name = 'DoubleVerify'

    def scrape(self):
        super().scrape()

