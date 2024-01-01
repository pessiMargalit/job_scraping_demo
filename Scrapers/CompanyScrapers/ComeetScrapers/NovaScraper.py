
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class NovaScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/nova/A5.007"
    name = "nova"

    def scrape(self):
        super().scrape()

    