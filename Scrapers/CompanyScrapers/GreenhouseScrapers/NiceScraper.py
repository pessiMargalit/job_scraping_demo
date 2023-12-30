
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class NiceScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/nicehealthcare"
    name = 'NICE'

    def scrape(self):
        super().scrape()

