
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class SundayskyScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/sundaysky/71.000"
    name = "SundaySky"

    def scrape(self):
        super().scrape()

    