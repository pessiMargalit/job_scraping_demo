
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class RedpandaScraper(GreenhouseScraper):
    official_url = "https://redpanda.com/careers"
    url = "https://boards.greenhouse.io/redpandadata"
    name = 'Redpanda'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


RedpandaScraper().check_self()
