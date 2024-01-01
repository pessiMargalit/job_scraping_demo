
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class PtcScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/ptc/32.005"
    name = "PTC"

    def scrape(self):
        super().scrape()

    