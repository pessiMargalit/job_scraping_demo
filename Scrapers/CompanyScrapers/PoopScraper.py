from Scrapers.Scraper import Scraper


class ExampleScraper(Scraper):
    name = 'Example'
    url = 'example.com'

    def scrape(self):
        soup = self.scraping_unit(self.url)

        pass