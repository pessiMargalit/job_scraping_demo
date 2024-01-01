
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class MccannScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/mccann/33.00C"
    name = "McCann"

    def scrape(self):
        super().scrape()

    