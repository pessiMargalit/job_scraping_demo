
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class KeterScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/keter-north-america/E3.001"
    name = "Keter"

    def scrape(self):
        super().scrape()

    