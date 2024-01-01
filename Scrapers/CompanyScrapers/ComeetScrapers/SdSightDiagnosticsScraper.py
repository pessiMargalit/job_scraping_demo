
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class SdsightdiagnosticsScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/sight/45.006"
    name = "SD Sight Diagnostics"

    def scrape(self):
        super().scrape()

    