from urllib.parse import urljoin

from Scrapers.Scraper import *


class HelixScraper(Scraper):
    name = 'helix'
    url = 'https://www.helixlinear.com/careers/'
    location = 'San Mateo, 101 S Ellsworth Ave, United States'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'document-item'}):
            job_meta_data = div_tag.findNext('a')
            link = urljoin(self.url, job_meta_data['href'])
            title = job_meta_data.text.strip()
            description = div_tag.findNext('p').findNext('p').text.strip()
            self.positions.append(self.Position(
                title=title,
                link=link,
                content=description
            ))
