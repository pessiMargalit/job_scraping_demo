from urllib.parse import urljoin
from Scrapers.Scraper import *


class BrownHotelsScraper(Scraper):
    url = 'https://brownhotels.com/he/workwithus'
    name = 'Brown hotels'
    location = 'כל הארץ'

    def __init__(self):
        super(BrownHotelsScraper, self).__init__()

    def scrape(self):
        soup = self.scraping_unit(self.url)
        i = 1
        for div in soup.find_all('div', {"class": 'item_text_wrapper'})[1:-1]:
            title = div.findNext('h3', {'class': 'rteright'})
            link = urljoin(self.url, f'#{i}')
            i += 1
            self.positions.append(self.Position(
                title=title.text,
                link=link
            ))


BrownHotelsScraper().check_self()
