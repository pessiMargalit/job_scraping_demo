
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class CellebriteScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/Cellebrite/C3.00F"
    name = "Cellebrite"

    def scrape(self):
        super().scrape()

    