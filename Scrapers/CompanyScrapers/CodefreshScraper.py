
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class CodefreshScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/codefresh"
    name = 'Codefresh'

    def scrape(self):
        super().scrape()

CodefreshScraper().check_self()