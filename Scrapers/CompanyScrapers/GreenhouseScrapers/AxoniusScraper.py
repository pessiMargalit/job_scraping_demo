
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class AxoniusScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/embed/job_board?for=Axonius"
    name = 'Axonius'

    def scrape(self):
        super().scrape()

