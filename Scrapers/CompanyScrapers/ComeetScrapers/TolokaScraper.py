
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class TolokaScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/toloka/98.00B"
    name = "Toloka"

    def scrape(self):
        super().scrape()

    