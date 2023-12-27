
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class RiskifiedScraper(GreenhouseScraper):
    official_url = "https://www.riskified.com/careers/"
    url = "https://boards.greenhouse.io/embed/job_board?for=riskified"
    name = 'Riskified'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


RiskifiedScraper().check_self()
