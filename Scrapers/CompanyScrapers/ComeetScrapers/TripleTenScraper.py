
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class TripletenScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/tripleten/98.008"
    name = "triple ten"

    def scrape(self):
        super().scrape()

    