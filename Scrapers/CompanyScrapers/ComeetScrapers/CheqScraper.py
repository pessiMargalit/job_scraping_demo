
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class CheqScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/cheq/65.005"
    name = "cheq"

    def scrape(self):
        super().scrape()

    