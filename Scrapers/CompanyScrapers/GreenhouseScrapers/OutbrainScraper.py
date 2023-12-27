
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class OutbrainScraper(GreenhouseScraper):
    official_url = "https://www.outbrain.com/careers/"
    url = "https://boards.eu.greenhouse.io/outbraininc"
    name = 'Outbrain'

    def scrape(self):
        super().scrape()


OutbrainScraper().check_self()
