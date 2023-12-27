
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class MESHPaymentsScraper(GreenhouseScraper):
    official_url = "https://meshpayments.com/careers/"
    url = "https://boards.greenhouse.io/meshpayments"
    name = 'MESH Payments'

    def scrape(self):
        super().scrape()


MESHPaymentsScraper().check_self()
