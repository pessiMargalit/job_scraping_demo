
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class MeshPaymentsScraper(GreenhouseScraper):
    url = "https://boards.greenhouse.io/meshpayments"
    name = 'MESH Payments'

    def scrape(self):
        super().scrape()

