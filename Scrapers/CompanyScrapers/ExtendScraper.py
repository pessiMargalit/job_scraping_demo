from urllib.parse import urljoin

from Scrapers.Scraper import Scraper


class ExtendScraper(Scraper):
    name = 'EXTEND'
    url = 'https://defense.xtend.me/about/careers/'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('a', {'class': 'comeet-position'}):

            title = a_tag.findNext('div', {"class": 'comeet-position-name'})
            location = a_tag.findNext('div', {'class': 'comeet-position-meta'})
            link=a_tag['href']
            self.positions.append(self.Position(
                title=title.text,
                link=urljoin(self.url, link),
                location=location.text
            ))
