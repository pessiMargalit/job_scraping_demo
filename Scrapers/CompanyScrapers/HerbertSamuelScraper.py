from urllib.parse import urljoin
from Scrapers.Scraper import *


class HerbertSamuelScraper(Scraper):
    url = 'https://herbertsamuel.com/career/'
    name = 'HerbertSamuel'
    location = 'כל הארץ'

    def __init__(self):
        super(HerbertSamuelScraper, self).__init__()

    def scrape(self):
        soup = self.scraping_unit(self.url)
        i = 1
        for div in soup.find_all('div', {"class": 'elementor-widget-wrap elementor-element-populated'})[16:-17]:
            title = div.findNext('h2', {'class': 'elementor-heading-title elementor-size-default'})
            self.positions.append(self.Position(
                title=title.text,
                link=urljoin(self.url,f'#{i}')
            ))
            i += 1

