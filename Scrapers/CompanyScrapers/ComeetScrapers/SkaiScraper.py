
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class SkaiScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/skai/22.00A"
    name = "Skai"

    def scrape(self):
        super().scrape()

    