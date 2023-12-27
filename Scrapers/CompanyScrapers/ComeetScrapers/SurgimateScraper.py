
from ScrapingTools.OutsourceTools.Comeet.BaseScraper import ComeetScraper


class SurgimateScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/surgimate/B7.00D"
    name = "Surgimate"

    def scrape(self):
        super().scrape()

    