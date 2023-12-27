
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class SimplyScraper(GreenhouseScraper):
    official_url = "https://www.hellosimply.com/careers"
    url = "https://simplygreenhouse.com/"
    name = 'Simply'

    def scrape(self):
        super().scrape()


SimplyScraper().check_self()
