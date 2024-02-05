from urllib.parse import urljoin
from Scrapers.Scraper import *


class OrientHotelScraper(Scraper):
    url = 'https://www.isrotel.co.il/careers/job/jerusalem-or/'
    name = 'Orient'
    location = 'jerusalem'

    def __init__(self):
        super(OrientHotelScraper, self).__init__()

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div in soup.find_all('div', {"class": 'col-sm-4 pb-5 mb-4'}):
            title = div.findNext('h3')
            link = div.findNext('a')['href']
            link = urljoin(self.url, link)
            self.positions.append(self.Position(
                title=title.text.strip(),
                link=link
            ))


OrientHotelScraper().check_self()
