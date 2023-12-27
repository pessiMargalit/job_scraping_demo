
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class DeepMindScraper(GreenhouseScraper):
    official_url = "https://deepmind.google/about/careers/#open-roles"
    url = "https://boards.greenhouse.io/deepmind"
    name = 'DeepMind'

    def scrape(self):
        super().scrape()


DeepMindScraper().check_self()
