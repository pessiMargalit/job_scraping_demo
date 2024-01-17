from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Scrapers.Scraper import Scraper

TIMEOUT_IN_SECONDS = 10


class ClarivateScraper(Scraper):
    name = 'Clarivate'
    url = 'https://careers.clarivate.com/search/searchjobs'
    location = 'Jerusalem'
    NUMBER_JOBS_PER_PAGE = 12

    @staticmethod
    def find_max_iteration(number_of_jobs):
        return number_of_jobs // ClarivateScraper.NUMBER_JOBS_PER_PAGE

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'jtable-data-row'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        number_of_jobs = int(soup.find('span', {'class': 'jtable-page-info'}).text.split()[-1])
        max_iteration = ClarivateScraper.find_max_iteration(number_of_jobs)
        counter = 0
        while counter < max_iteration:
            counter += 1
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
            
            # btn = driver.find_element((By.CLASS_NAME, 'jtable-page-number-next-mobile ui-button ui-state-default'))
            # btn.click()


