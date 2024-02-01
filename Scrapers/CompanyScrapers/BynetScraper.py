from Scrapers.Scraper import *


class BynetScraper(Scraper):
    name = 'Bynet'
    url = 'https://www.bynet.co.il/open-positions/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        i = 1
        for div in soup.findAll('article', {'class': 'job-wrapper'}):
            title = div.findNext('h3', {'class': 'job-role'})
            location = div.findNext('span', {'class': 'job-location-wrapper'})
            link = f'{self.url}#{i}'
            i += 1
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=link if link else self.url,
                location=location.text.strip() if location else None,
            ))
