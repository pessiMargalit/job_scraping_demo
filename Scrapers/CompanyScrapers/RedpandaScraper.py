
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class RedpandaScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/redpandadata"
    name = 'Redpanda'

    def scrape(self):
        super().scrape()

