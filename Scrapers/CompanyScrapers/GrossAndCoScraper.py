from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class GrossAndCoScraper(Scraper):
    name = 'Gross & Co'
    url = 'https://www.gkh-law.com/career/'
    location = "ירושלים"

    def get_positions_lst(self, url):
        soup = self.scraping_unit(url)
        positions = soup.findAll("button", {"class": "accordion accordion_2"})
        return positions

    def scrape(self):
        positions = self.get_positions_lst(self.url)
        positions.extend(self.get_positions_lst('https://www.gkh-law.com/he/career/'))
        for pos in positions:
            title = pos
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
            ))
