
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class HillelScraper(GreenhouseScraper):
    official_url = "https://www.hillel.org/work-at-hillel/"
    url = "https://boards.greenhouse.io/hillel"
    name = 'Hillel'

    def scrape(self):
        super().scrape()


HillelScraper().check_self()
