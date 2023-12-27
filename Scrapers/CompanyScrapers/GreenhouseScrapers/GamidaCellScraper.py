
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class GamidaCellScraper(GreenhouseScraper):
    official_url = "https://www.gamida-cell.com/careers/"
    url = "https://boards.greenhouse.io/gamidacell"
    name = 'Gamida Cell'

    def scrape(self):
        super().scrape()


GamidaCellScraper().check_self()
