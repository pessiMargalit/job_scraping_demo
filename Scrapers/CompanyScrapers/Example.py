from Scrapers.Scraper import Scraper


class PoopScraper(Scraper):
    name = 'Poop'
    url = 'example.com'

    def scrape(self):
        soup = self.scraping_unit(self.url)

        pass