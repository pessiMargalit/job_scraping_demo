
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class UnityScraper(GreenhouseScraper):
    official_url = "https://careers.unity.com/"
    url = "https://unity.greenhouse.io/"
    name = 'Unity'

    def scrape(self):
        super().scrape()


UnityScraper().check_self()
