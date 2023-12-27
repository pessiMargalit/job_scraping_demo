
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class CodefreshScraper(GreenhouseScraper):
    official_url = "https://codefresh.io/careers/"
    url = "https://codefresh.io/"
    name = 'Codefresh'

    def scrape(self):
        super().scrape()


CodefreshScraper().check_self()
