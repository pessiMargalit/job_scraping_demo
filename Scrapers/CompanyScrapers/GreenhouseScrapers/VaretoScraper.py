
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class VaretoScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/vareto"
    name = 'Vareto'

    def scrape(self):
        super().scrape()

