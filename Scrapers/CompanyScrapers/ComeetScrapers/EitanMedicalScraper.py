
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class EitanmedicalScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/eitanmedical/C6.00F"
    name = "Eitan Medical"

    def scrape(self):
        super().scrape()

    