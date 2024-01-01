
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class WiliotScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/wiliot/F6.003"
    name = "Wiliot"

    def scrape(self):
        super().scrape()

    