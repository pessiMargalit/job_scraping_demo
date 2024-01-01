
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class JvpScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/jvp/35.00E"
    name = "JVP"

    def scrape(self):
        super().scrape()

    