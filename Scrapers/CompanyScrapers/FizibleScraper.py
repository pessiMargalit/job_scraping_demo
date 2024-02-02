
from urllib.parse import urljoin

from Scrapers.Scraper import *


class FizibleScraper(Scraper):
    name = 'Fizible'
    url = 'https://www.vizible.zone/careers-viziblezone-protecting-vulnerable-road-users'
    location = 'HQ'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'collection-item-2 w-dyn-item'}):
            title = div_tag.findNext('h1', {'class': 'text-block-12'}).text
            link = div_tag.findNext('a', {'class': 'link-block w-inline-block'})['href']
            if self.url not in link:
                link = urljoin(self.url, link)
            self.positions.append(self.Position(
                title=title,
                link=link,
            ))


