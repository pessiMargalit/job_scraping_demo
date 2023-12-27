
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class SisenseScraper(GreenhouseScraper):
    official_url = "https://www.sisense.com/careers/"
    url = "https://boards.greenhouse.io/embed/job_board?for=sisense"
    name = 'Sisense'

    def scrape(self):
        super().scrape()


SisenseScraper().check_self()
