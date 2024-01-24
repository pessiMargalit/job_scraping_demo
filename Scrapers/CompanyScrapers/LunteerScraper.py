
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class LunteerScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/volunteer"
    name = 'Lunteer'

    def scrape(self):
        super().scrape()

