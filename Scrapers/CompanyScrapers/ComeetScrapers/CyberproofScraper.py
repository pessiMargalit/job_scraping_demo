
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class CyberproofScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/cyberproof/75.00F"
    name = "CyberProof"

    def scrape(self):
        super().scrape()

    