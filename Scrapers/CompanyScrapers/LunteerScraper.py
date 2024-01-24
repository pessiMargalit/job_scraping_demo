
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class LunteerScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/volunteer/jobs/1494225"
    name = 'Lunteer'

    def scrape(self):
        super().scrape()

