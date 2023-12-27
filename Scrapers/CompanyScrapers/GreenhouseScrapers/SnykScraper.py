
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class SnykScraper(GreenhouseScraper):
    official_url = "https://snyk.io/careers/"
    url = "https://boards.greenhouse.io/snyk"
    name = 'Snyk'

    def scrape(self):
        super().scrape()


SnykScraper().check_self()
