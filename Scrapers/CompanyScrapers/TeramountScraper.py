from Scrapers.Scraper import *
import re


class TeramountScraper(Scraper):
    name = 'Teramount'
    url = 'https://teramount.com/careers/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        jobs = soup.find_all('div', {'class': "item"})
        for job in jobs:
            title = job.find_next('h4')
            content = job.find_next('div', {'class': 'text editor'})
            pattern = re.compile(r'^Our address\s*:\s*(.*)$', re.MULTILINE)
            location = pattern.search(content.text).group(1)

            self.positions.append(self.Position(
                title=title.text if title else None,
                location=location if location else None,
                content=content.text if content else None
            ))