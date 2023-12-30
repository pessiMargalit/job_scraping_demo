
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class SouthworksScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/southworks"
    name = 'SOUTHWORKS'

    def scrape(self):
        super().scrape()

