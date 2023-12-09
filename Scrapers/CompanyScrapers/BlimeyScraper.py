from Scrapers.Scraper import *


class BlimeyScraper(Scraper):
    url = 'http://theholycity.blimey.tv/index.php/jobs/'
    name = 'Blimey'

    def __init__(self):
        
        super(BlimeyScraper, self).__init__()

    def scrape(self):
        # Implement using BeautifulSoup, wait for the page to load using selenium
        pass
