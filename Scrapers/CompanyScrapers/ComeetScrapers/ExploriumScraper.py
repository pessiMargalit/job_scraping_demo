
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class ExploriumScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/explorium/B4.00E"
    name = "explorium"

    def scrape(self):
        super().scrape()

    