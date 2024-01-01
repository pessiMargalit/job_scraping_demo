
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class ImubitScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/imubit/84.008"
    name = "Imubit"

    def scrape(self):
        super().scrape()

    