
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class ChronosphereScraper(GreenhouseScraper):
    official_url = "https://chronosphere.io/careers/"
    url = "https://boards.greenhouse.io/chronosphere"
    name = 'Chronosphere'

    def scrape(self):
        super().scrape()


ChronosphereScraper().check_self()
