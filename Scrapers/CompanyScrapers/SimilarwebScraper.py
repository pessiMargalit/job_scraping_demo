
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class SimilarwebScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/similarweb"
    name = 'Similarweb'

    def scrape(self):
        super().scrape()

