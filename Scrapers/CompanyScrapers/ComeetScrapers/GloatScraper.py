
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class GloatScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/gloat/E5.000"
    name = "Gloat"

    def scrape(self):
        super().scrape()

    