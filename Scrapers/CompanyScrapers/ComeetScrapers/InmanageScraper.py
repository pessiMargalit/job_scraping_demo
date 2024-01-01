
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class InmanageScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/inmanage/B7.006"
    name = "InManage"

    def scrape(self):
        super().scrape()

    