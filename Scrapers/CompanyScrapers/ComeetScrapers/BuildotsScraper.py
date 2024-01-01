
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class BuildotsScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/buildots/36.004"
    name = "buildots"

    def scrape(self):
        super().scrape()

    