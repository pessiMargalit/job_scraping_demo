
from ScrapingTools.OutsourceTools.Comeet.BaseScraper import ComeetScraper


class CognyteScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/cognyte/F2.009"
    name = "Cognyte"

    def scrape(self):
        super().scrape()

    