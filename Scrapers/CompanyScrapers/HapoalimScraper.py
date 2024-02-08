import re
from urllib.parse import urljoin

from Scrapers.Scraper import Scraper


class HapoalimScraper(Scraper):
    name = "hapoalim"
    url = "https://www.bankhapoalim.co.il/he/jobs-site/lobby"

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('a', {'class': 'views-row job'}):
            title = a_tag.findNext('div', {'class': 'job-name'}).text.strip()
            # remove unclear numbers
            title = re.sub(r'\d+', '', title)
            link = urljoin(self.url, a_tag['href'])
            location = a_tag.findNext('div', {'class': 'job-area'}).text.strip()
            self.positions.append(self.Position(
                title=title,
                location=location,
                link=link
            ))