
from Scrapers.Scraper import *


class LightricksScraper(Scraper):
    name = 'Lightricks'

    def scrape(self):
        # Implement using requests, find a specific request in the site's network tab (XHR/fetch tab)
        # should be somehitng like:
        # response = requests.get(SOME_URL)
        #
        # response_json = response.json()
        # then we need to parse that json
        pass