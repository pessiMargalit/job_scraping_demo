
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class RiversideScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/riverside-fm/66.009"
    name = "RiverSide"

    def scrape(self):
        super().scrape()

    