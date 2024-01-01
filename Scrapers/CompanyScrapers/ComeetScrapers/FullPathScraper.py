
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class FullpathScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/fullpath/54.002"
    name = "full path"

    def scrape(self):
        super().scrape()

    