
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class GauzyScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/gauzy/C5.003"
    name = "Gauzy"

    def scrape(self):
        super().scrape()

    