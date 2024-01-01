
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class CymotiveScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/cymotive/F1.008"
    name = "Cymotive"

    def scrape(self):
        super().scrape()

    