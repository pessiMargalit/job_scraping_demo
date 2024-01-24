
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class MavenclinicScraper(GreenhouseScraper):
    url = "https://boards.greenhouse.io/mavenclinic"
    name = 'Maven Clinic'

    def scrape(self):
        super().scrape()

