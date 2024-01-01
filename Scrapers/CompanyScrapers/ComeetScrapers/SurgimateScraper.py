
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class SurgimateScraper(ComeetScraper):
    url = "https://www.surgimate.com/hiring/"
    name = "Surgimate"

    def scrape(self):
        super().scrape()

    