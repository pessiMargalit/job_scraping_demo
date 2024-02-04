from Scrapers.Scraper import *


class CalypsaScraper(Scraper):
    name = 'Calypsa'
    url = 'https://calypsa.com/careers'
    base_url = 'https://calypsa.com'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        div_positions = soup.find('div', {'class': 'main-page-1Ex'})
        for div_position in div_positions.findAll('div', {'class': 'text-root-1y8'}):
            title = div_position.findNext('a')
            if title:
                self.positions.append(self.Position(
                    title=title.text if title else None,
                    link=f"{self.base_url}{title['href']}" if title else None,
                    location=self.location
                ))

