
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class VpgsensorsScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/vpgsensors/C8.009"
    name = "VPG Sensors"

    def scrape(self):
        super().scrape()

    