
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class FeedvisorScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/feedvisor/11.00A"
    name = "feedvisor"

    def scrape(self):
        super().scrape()

    