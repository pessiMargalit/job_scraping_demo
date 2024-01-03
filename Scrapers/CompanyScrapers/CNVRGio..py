from Scrapers.Scraper import *


class ArmoScraper(Scraper):
    name = 'cnvrg.io'
    url = 'https://cnvrg.io/Careers/'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        i = 1
        for div in soup.findAll('a', {'class': 'comeet-position'}):
            title = div.findNext('div', {'class': 'comeet-position-name'})
            location = div.findNext('div', {'class': 'comeet-position-meta'})
            link = title.findNext('a')['href']
            # link = link['href']
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
                link=link if link else self.url,
                location=location.text.strip() if location else None,
            ))


ArmoScraper().check_self()
