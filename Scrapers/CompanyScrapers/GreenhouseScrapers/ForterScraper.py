
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class ForterScraper(GreenhouseScraper):
    official_url = "https://www.forter.com/careers/"
    url = "https://boards.greenhouse.io/forter"
    name = 'Forter'

    def scrape(self):
        super().scrape()


ForterScraper().check_self()
