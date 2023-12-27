
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class JFrogScraper(GreenhouseScraper):
    official_url = "https://join.jfrog.com/"
    url = "https://boards.greenhouse.io/embed/job_board?for=jfrog"
    name = 'JFrog'

    def scrape(self):
        super().scrape()


JFrogScraper().check_self()
