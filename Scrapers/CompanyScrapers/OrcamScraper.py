from urllib.parse import urljoin

from Scrapers.Scraper import *


class OrcamScraper(Scraper):
    name = 'orcam'
    url = 'https://careers.orcam.com/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('a', {'class': 'col-md-6'}):
            title = a_tag.findNext('h5', {'class': 'title'}).text.strip()
            link = urljoin(self.url,a_tag['href'])
            location = a_tag.findNext('li', {'class': 'location'}).text.strip()
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))
