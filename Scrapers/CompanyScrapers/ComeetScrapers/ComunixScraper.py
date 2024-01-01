
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class ComunixScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/comunix/86.006"
    name = "Comunix"

    def scrape(self):
        super().scrape()

    