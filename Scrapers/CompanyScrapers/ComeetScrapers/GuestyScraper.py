
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class GuestyScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/guesty/10.000"
    name = "Guesty"

    def scrape(self):
        super().scrape()

    