from urllib.parse import urljoin
from Scrapers.Scraper import *


class AfrikaIsraelHotelsScraper(Scraper):
    url = 'https://www.afi-hotels.co.il/jobs'
    name = 'Afi hotels'
    location = 'כל הארץ'

    def __init__(self):
        super(AfrikaIsraelHotelsScraper, self).__init__()

    def scrape(self):
        soup = self.scraping_unit(self.url)
        i = 1
        for div in soup.find_all('div', {"class": 'job-item'}):
            title = div.findNext('h3', {'class': 'job-name'})
            link = urljoin(self.url, f'#{i}')
            i += 1
            self.positions.append(self.Position(
                title=title.text.strip(),
                link=link
            ))


