import re

from Scrapers.Scraper import *


class MidragScraper(Scraper):
    name = "Midrag"
    url = 'https://www.midrag.co.il/content/article/1100'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find_all('a', href=lambda href: href and href.startswith('/content/Article/1100#'))

        for job in careers:
            match = re.search(r'#(\w+)', job['href'])

            if match:
                link = f"{self.url}#{match.group(1)}"
            else:
                link = f"{self.url}"
            title = job.text.strip()
            self.positions.append(self.Position(
                title=title,
                link=link
            ))

