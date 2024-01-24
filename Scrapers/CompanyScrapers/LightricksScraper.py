
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class LightricksScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/embed/job_board?for=lightricks"
    name = 'Lightricks'

    def scrape(self):
        super().scrape()

