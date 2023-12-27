
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class VaretoScraper(GreenhouseScraper):
    official_url = "https://www.vareto.com/careers"
    url = "https://boards.greenhouse.io/vareto"
    name = 'Vareto'

    def scrape(self):
        super().scrape()


VaretoScraper().check_self()
