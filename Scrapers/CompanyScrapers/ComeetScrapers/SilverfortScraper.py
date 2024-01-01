
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class SilverfortScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/silverfort/54.007"
    name = "SilverFort"

    def scrape(self):
        super().scrape()

    