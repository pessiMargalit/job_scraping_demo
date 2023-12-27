
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class SimilarwebScraper(GreenhouseScraper):
    official_url = "https://www.similarweb.com/corp/careers/"
    url = "https://boards.greenhouse.io/similarweb"
    name = 'Similarweb'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


SimilarwebScraper().check_self()
