
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class DoubleVerifyScraper(GreenhouseScraper):
    official_url = "https://doubleverify.com/careers/"
    url = "https://boards.greenhouse.io/doubleverify"
    name = 'DoubleVerify'

    def scrape(self):
        super().scrape()


DoubleVerifyScraper().check_self()
