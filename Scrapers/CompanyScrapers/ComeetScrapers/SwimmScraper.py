
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class SwimmScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/swimm/56.007"
    name = "Swimm"

    def scrape(self):
        super().scrape()

    