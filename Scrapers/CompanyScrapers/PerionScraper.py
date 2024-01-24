
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class PerionScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/perionnetworkltd"
    name = 'Perion'

    def scrape(self):
        super().scrape()

