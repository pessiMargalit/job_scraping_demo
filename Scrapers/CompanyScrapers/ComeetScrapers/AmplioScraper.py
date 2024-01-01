
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class AmplioScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/amplio/06.00C"
    name = "Amplio"

    def scrape(self):
        super().scrape()

    