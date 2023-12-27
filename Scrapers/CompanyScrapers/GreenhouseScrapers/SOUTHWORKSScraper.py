
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class SOUTHWORKSScraper(GreenhouseScraper):
    official_url = "https://www.southworks.com/careers"
    url = "https://boards.greenhouse.io/southworks"
    name = 'SOUTHWORKS'

    def scrape(self):
        super().scrape()


SOUTHWORKSScraper().check_self()
