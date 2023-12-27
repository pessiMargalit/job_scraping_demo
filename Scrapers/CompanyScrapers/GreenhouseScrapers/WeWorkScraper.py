
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class WeWorkScraper(GreenhouseScraper):
    official_url = "https://careers.wework.com/"
    url = "https://boards.greenhouse.io/wework"
    name = 'WeWork'

    def scrape(self):
        super().scrape()


WeWorkScraper().check_self()
