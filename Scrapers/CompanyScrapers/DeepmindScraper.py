
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class DeepmindScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/deepmind"
    name = 'DeepMind'

    def scrape(self):
        super().scrape()

