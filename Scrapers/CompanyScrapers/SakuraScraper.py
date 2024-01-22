from urllib.error import URLError
from urllib.parse import urljoin

from Scrapers.Scraper import *


class SakuraScraper(Scraper):
    name = 'Sakura'
    url = 'https://career.sakura.eu/https://career.sakura.eu/'

    def scrape(self):
        try:
            soup = self.scraping_unit(self.url)
            for div_tag in soup.findAll('div', {'class': 'sc-6exb5d-0 eGKXeh'}):
                a_tag = div_tag.findNext('a', {'class': 'sc-6exb5d-1 idLjgt'})
                title = a_tag.text.strip()
                link = urljoin(self.url, a_tag['href'])
                location = div_tag.find_next('span', {'class': 'custom-css-style-job-location'}).text.strip()
                self.positions.append(self.Position(
                    title=title,
                    link=link,
                    location=location
                ))
        except URLError as e:
            print(f"Error: {e}")


