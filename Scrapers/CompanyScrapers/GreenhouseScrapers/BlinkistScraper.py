
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class BlinkistScraper(GreenhouseScraper):
    official_url = "https://www.blinkist.com/en/jobs"
    url = "https://boards.eu.greenhouse.io/blinkist"
    name = 'Blinkist'

    def scrape(self):
        super().scrape()


BlinkistScraper().check_self()
