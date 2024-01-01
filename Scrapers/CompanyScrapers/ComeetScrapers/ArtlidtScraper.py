
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class ArtlidtScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/artlist/85.003"
    name = "Artlidt"

    def scrape(self):
        super().scrape()

    