
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class BluevineScraper(GreenhouseScraper):
    official_url = "https://www.bluevine.com/careers"
    url = "https://boards.greenhouse.io/bluevineus"
    name = 'Bluevine'

    def scrape(self):
        super().scrape()


BluevineScraper().check_self()
