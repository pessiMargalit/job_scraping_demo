
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class PagayaScraper(GreenhouseScraper):
    official_url = "https://pagaya.com/careers/"
    url = "https://boards.greenhouse.io/pagaya"
    name = 'Pagaya'

    def scrape(self):
        super().scrape()


PagayaScraper().check_self()
