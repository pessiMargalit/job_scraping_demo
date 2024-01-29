from Scrapers.Scraper import *


class AboulafiaScraper(Scraper):
    name = 'Aboulafia'
    url = 'https://aboulafia.co.il/wanted/'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all('p', {'dir': 'ltr'})
        for pos in positions[1:]:
            title = pos.text if pos else None
            self.positions.append(self.Position(
                title=title
            ))
