
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class IfmdeveloperScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/matrix-ifs/19.00F/ifm-developer/43.04B"
    name = "Ifm-Developer"

    def scrape(self):
        super().scrape()

    