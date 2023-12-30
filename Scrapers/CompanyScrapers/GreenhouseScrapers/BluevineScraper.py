
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class BluevineScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/bluevineus"
    name = 'Bluevine'

    def scrape(self):
        super().scrape()

