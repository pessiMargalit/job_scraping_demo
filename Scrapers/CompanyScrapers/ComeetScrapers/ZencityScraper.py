
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class ZencityScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/zencity/56.00B/"
    name = "Zencity"

    def scrape(self):
        super().scrape()

    