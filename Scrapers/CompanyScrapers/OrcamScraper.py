from urllib.parse import urljoin

from Scrapers.Scraper import *


class OrcamScraper(Scraper):
    name = 'Orcam'
    url = 'https://careers.orcam.com/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for job in soup.findAll('div', {'class': 'sc-uzptka-1 ifQvfy'}):
            details = job.findNext('a', {'class': 'sc-6exb5d-1 hftbaU'})
            title = details.text
            link = urljoin(self.url, details['href'])
            location = job.findNext('span', {'class': 'sc-6exb5d-4 knWhYe'}).text
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))
