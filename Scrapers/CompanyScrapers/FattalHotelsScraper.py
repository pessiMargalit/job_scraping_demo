from urllib.parse import urljoin
from Scrapers.Scraper import *


class FattalHotelsScraper(Scraper):
    url = 'https://www.fattal.co.il/jobs'
    name = 'Fattal hotels'
    location = 'jerusalem'

    def __init__(self):
        super(FattalHotelsScraper, self).__init__()

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div in soup.find_all('div', {"class": 'job'}):
            title = div.findNext('div', {'class': 'name'})
            self.positions.append(self.Position(
                title=title.text.strip(),
                link=self.url
            ))


