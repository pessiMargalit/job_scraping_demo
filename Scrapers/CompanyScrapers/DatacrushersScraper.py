from Scrapers.Scraper import *


class DatacrushersScraper(Scraper):
    name = 'Datacrushers'
    url = 'https://www.datacrushers.com/hiring/'
    location = "ירושלים"

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.findAll('div', {'class': "fusion-column-wrapper"})
        for pos in positions:
            title = pos.findNext('div', {'class': 'fusion-title'})
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
            ))
