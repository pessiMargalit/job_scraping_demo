
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class Pax8Scraper(GreenhouseScraper):
    official_url = "https://www.pax8.com/en-us/careers/"
    url = "https://boards.greenhouse.io/embed/job_board?for=pax8&b=https%3A%2F%2Fwww.pax8.com%2Fen-us%2Fcareers%2F"
    name = 'Pax8'

    def scrape(self):
        super().scrape()


Pax8Scraper().check_self()
