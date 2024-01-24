
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class SnykScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/snyk"
    name = 'Snyk'

    def scrape(self):
        super().scrape()

