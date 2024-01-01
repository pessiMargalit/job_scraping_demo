
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class TangoScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/tango/B7.007"
    name = "Tango"

    def scrape(self):
        super().scrape()

    