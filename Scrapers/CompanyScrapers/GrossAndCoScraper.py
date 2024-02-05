from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class GrossAndCoScraper(Scraper):
    name = 'Gross & Co'
    url = 'https://www.gkh-law.com/career/'

    def scrape_unit(self, url):
        soup = self.scraping_unit(url)
        positions = soup.findAll("button", {"class": "accordion accordion_2"})
        for pos in positions:
            title = pos
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
            ))

    def scrape(self):
        self.scrape_unit(self.url)
        self.scrape_unit('https://www.gkh-law.com/he/career/')


GrossAndCoScraper().check_self()
