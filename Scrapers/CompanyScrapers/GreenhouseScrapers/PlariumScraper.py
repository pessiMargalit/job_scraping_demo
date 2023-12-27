
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class PlariumScraper(GreenhouseScraper):
    official_url = "https://company.plarium.com/en/career/"
    url = "https://boards.eu.greenhouse.io/plariumgloballtd/jobs/4215649101"
    name = 'Plarium'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


PlariumScraper().check_self()
