
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class NonameScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/noname/86.001"
    name = "noname"

    def scrape(self):
        super().scrape()

    