
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class MoonactiveScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/moonactive/A2.00C"
    name = "Moonactive"

    def scrape(self):
        super().scrape()

    