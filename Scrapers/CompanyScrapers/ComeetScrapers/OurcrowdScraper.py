
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class OurcrowdScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/ourcrowd/D3.00A"
    name = "ourcrowd"

    def scrape(self):
        super().scrape()

    