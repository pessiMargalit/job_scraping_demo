from Scrapers.Scraper import *


class BankYahavScraper(Scraper):
    name = 'בנק יהב'
    url = 'https://www.bank-yahav.co.il/about/jobs/'
    location = 'ירושלים'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all('div', attrs={'class': "career__block"})
        for pos in positions:
            title = pos.findNext('div', {'class': 'desc__name'})
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
            ))
