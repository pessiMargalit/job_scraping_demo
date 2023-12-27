
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class TallyScraper(GreenhouseScraper):
    official_url = "https://tallysolutions.com/careers/opportunities/"
    url = "https://boards.greenhouse.io/tally"
    name = 'Tally'

    def scrape(self):
        super().scrape()


TallyScraper().check_self()
