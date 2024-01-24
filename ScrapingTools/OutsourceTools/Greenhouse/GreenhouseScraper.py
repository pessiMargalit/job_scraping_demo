from Scrapers.Scraper import *


class GreenhouseScraper(Scraper):
    base_url = 'https://boards.greenhouse.io/'
    url = 'https://boards.greenhouse.io/'
    name = 'Greenhouse'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for position_div in soup.findAll('div', {'class': 'opening'}):
            title = position_div.findNext('a')
            location = position_div.findNext('span', {'class': 'location'})
            link = title['href'] if title else None
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
                link=f'{self.base_url}{link}',
                location=location.text.strip() if location else None
            ))
