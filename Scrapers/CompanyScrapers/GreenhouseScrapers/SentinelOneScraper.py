
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class SentinelOneScraper(GreenhouseScraper):
    official_url = "https://www.sentinelone.com/jobs/"
    url = "https://boards.greenhouse.io/embed/job_board?for=sentinellabs"
    name = 'SentinelOne'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


SentinelOneScraper().check_self()
