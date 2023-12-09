from Scrapers.Scraper import *


class ClalitScraper(Scraper):
    name = 'קופת חולים כללית'
    url = 'https://jobs.clalitapps.co.il/clalit/index.html?ci=0'

    def scrape(self):
        # Very hard to scrape, use selenium to wait for the page to load somehow
        # you can create a selenium driver using the self.selenium_url_maker(url) function
        # and then use BeautifulSoup to parse the driver.page_source
        # don't forget to wait for the page to load using WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(EC ... )
        pass
