
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class SecclScraper(GreenhouseScraper):
    official_url = "https://seccl.tech/careers/"
    url = "https://boards.eu.greenhouse.io/embed/job_board?for=seccltechnology&b=https%3A%2F%2Fseccl.tech%2Fcareers%2Frole%2Fqa-engineer%2F"
    name = 'Seccl'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


SecclScraper().check_self()
