from Scrapers.Scraper import *
from urllib.parse import quote

TIMEOUT_IN_SECONDS = 30


class MatrixScraper(Scraper):
    url = 'https://www.matrix.co.il/jobs/'
    name = 'matrix'
    location = 'ירושלים'

    def collect_urls(self):

        try:
            soup = self.scraping_unit(self.url)
            ul_tag = soup.find('ul', {'id': "jobs_category_list"})
            urls = [
                quote(li_tag.findNext('a')['href'], safe=':/') for i, li_tag in enumerate(ul_tag) if i % 2 != 0
            ]
        except (AttributeError, KeyError) as e:
            urls = []  # Empty list if an exception occurs
        return urls

    def scrape(self):
        positions_urls = MatrixScraper().collect_urls()
        for position_url in positions_urls:
            soup = self.scraping_unit(position_url)
            for div in soup.findAll('div', {'class': 'job-item'}):
                title = div.findNext('h2', {'class': 'job-title'})
                location = div.findNext('b', {'class': 'job-areas'})
                link = title.findNext('a')['href']
                if self.location in location.text:
                    self.positions.append(self.Position(
                        title=title.text if title else None,
                        link=link if link else self.url,
                        location=location.text if location else None,
                    ))


MatrixScraper().check_self()
