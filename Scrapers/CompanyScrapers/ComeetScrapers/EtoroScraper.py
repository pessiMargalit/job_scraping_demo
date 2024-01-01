
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class EtoroScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/etoro/41.009"
    name = "Etoro"

    def scrape(self):
        super().scrape()

    