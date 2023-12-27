
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class HandshakeScraper(GreenhouseScraper):
    official_url = "https://joinhandshake.com/careers/"
    url = "https://boards.greenhouse.io/embed/job_board?for=joinhandshake"
    name = 'Handshake'

    def scrape(self):
        super().scrape()


HandshakeScraper().check_self()
