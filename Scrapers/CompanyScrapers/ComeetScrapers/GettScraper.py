
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class GettScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/gett/A0.002"
    name = "Gett"

    def scrape(self):
        super().scrape()

    