
from ScrapingTools.OutsourceTools.Greenhouse.BaseScraper import GreenhouseScraper


class Blinkist(GreenhouseScraper): 
    url = "https://boards.eu.greenhouse.io/blinkist"
    name = 'Blinkist'

    def scrape(self):
        super().scrape()

