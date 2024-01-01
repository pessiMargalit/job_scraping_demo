
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class TrullionScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/trullion/07.000"
    name = "Trullion"

    def scrape(self):
        super().scrape()

    