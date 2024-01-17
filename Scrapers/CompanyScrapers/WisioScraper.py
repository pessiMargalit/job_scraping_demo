from Scrapers.Scraper import *

from bs4 import BeautifulSoup


class WisioScraper(Scraper):
    name = 'Wisio'
    url = 'https://www.wisio.com/careers'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        for div_tag in soup.findAll('div', {'id': "articleHeader"}):
            title = div_tag
            self.positions.append(self.Position(
                title=title.text,
                link=self.url

            ))


WisioScraper().check_self()
