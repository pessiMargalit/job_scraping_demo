from Scrapers.Scraper import *


class JoynedScraper(Scraper):
    name = 'Joyned'
    url = 'https://www.joyned.co/careers/'

    def scrape(self):
        # Implement using BeautifulSoup
        # should be pretty hard
        pass


JoynedScraper().check_self()
# JoynedScraper().update_in_bageldb()
