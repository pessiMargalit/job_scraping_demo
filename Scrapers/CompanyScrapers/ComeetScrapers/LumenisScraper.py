
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class LumenisScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/lumenis/A1.00C"
    name = "Lumenis"

    def scrape(self):
        super().scrape()

    