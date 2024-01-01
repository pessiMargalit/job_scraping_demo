
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class ActivefenceScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/activefence/D5.005"
    name = "ActiveFence"

    def scrape(self):
        super().scrape()

    