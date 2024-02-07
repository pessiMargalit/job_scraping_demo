from urllib.parse import urljoin
from Scrapers.Scraper import *


class CaesarHotelsScraper(Scraper):
    url = 'https://jobs.caesarhotels.co.il/%D7%93%D7%A8%D7%95%D7%A9%D7%99%D7%9D-%D7%91%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D'
    name = 'caesar'
    location = 'jerusalem'

    def __init__(self):
        super(CaesarHotelsScraper, self).__init__()

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div in soup.find_all('tr'):
            title = div.findNext('a')
            link = urljoin(self.url, title['href'])
            self.positions.append(self.Position(
                title=title.text.strip(),
                link=link
            ))



