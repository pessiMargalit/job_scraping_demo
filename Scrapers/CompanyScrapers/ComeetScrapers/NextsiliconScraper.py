
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class NextsiliconScraper(ComeetScraper):
    url = "https://www.nextsilicon.com/careers/"
    name = "NextSilicon"

    def scrape(self):
        super().scrape()

    