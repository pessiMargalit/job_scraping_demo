
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class LivepersonScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/liveperson"
    name = 'Liveperson'

    def scrape(self):
        super().scrape()

