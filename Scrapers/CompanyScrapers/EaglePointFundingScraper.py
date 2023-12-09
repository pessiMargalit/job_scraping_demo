from Scrapers.Scraper import *


class EaglePointFundingScraper(Scraper):
    name = 'Eagle Point Funding'
    url = 'https://www.eaglepointfunding.com/about'

    def scrape(self):
        # implement using requests
        # find a specific json request in the site's network tab (XHR/fetch tab)
        pass


EaglePointFundingScraper().check_self()
# EaglePointFundingScraper().update_in_bageldb()
