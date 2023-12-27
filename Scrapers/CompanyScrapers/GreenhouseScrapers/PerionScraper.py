
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class PerionScraper(GreenhouseScraper):
    official_url = "https://www.perion.com/careers/"
    url = "https://boards.greenhouse.io/perionnetworkltd"
    name = 'Perion'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


PerionScraper().check_self()
