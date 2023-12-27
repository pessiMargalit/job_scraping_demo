
from ScrapingTools.OutsourceTools.Greenhouse.BaseScraper import GreenhouseScraper


class Axonius(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/embed/job_board?for=Axonius"
    name = 'Axonius'

    def scrape(self):
        super().scrape()

