
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class AgoraScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/agora/08.007"
    name = "Agora"

    def scrape(self):
        super().scrape()

    