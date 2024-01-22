from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Scrapers.Scraper import Scraper

TIMEOUT_IN_SECONDS = 10


# exlilbris has no open jobs in Israel
class ExliblisScraper(Scraper):
    name = 'Exliblis'
    url = 'https://careers.clarivate.com/search/searchjobs'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'jtable-data-row'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for tr_tag in soup.findAll('tr', {'role': 'link'}):
            title = tr_tag.findNext('td', {'class': 'title-column'}).text
            link = tr_tag['data-href']
            location = tr_tag.findNext('td', {'class': 'city-state-column'}).text
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))