from Scrapers.Scraper import *


class CatchMediaScraper(Scraper):
    name = 'catchmedia'
    url = 'https://www.catchmedia.com/catch-media-company-careers.html'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        i = 1
        for div in soup.findAll('div', {'class': 'etl-info _4'}):
            title = div.findNext('h3', {'class': 'h4 green'})
            location = self.location
            link = f'{self.url}#{i}'
            i += 1
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=link if link else self.url,
                location=location.strip() if location else None,
            ))


