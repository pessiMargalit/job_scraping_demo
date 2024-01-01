
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class CitadelScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/citadel/33.003"
    name = "Citadel"

    def scrape(self):
        super().scrape()

    