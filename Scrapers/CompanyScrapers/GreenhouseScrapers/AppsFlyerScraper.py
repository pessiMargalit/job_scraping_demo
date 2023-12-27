
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class AppsFlyerScraper(GreenhouseScraper):
    official_url = "https://careers.appsflyer.com/"
    url = "https://appsflyer.greenhouse.io/"
    name = 'AppsFlyer'

    def scrape(self):
        super().scrape()


AppsFlyerScraper().check_self()
