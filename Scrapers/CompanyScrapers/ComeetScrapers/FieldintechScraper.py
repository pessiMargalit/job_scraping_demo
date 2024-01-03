
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class FieldintechScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/fieldintech/68.001"
    name = "fieldintech"

    def scrape(self):
        super().scrape()

    