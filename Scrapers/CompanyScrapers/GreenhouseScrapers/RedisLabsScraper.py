
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class RedisLabsScraper(GreenhouseScraper):
    official_url = "https://redis.com/company/careers/"
    url = "https://redis.com/company/careers/"
    name = 'Redis Labs'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


RedisLabsScraper().check_self()
