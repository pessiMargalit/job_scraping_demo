from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Scrapers.Scraper import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class KasperskyScraper(Scraper):
    name = 'Kaspersky'
    url = 'https://careers.kaspersky.com/vacancy'

    def specific_page_url(self, index):
        string_index = f"?page={index}"
        return urljoin(self.url, string_index)

    def find_max_iteration(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'vacancy-card'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        div_tag = soup.find('div', {'class': 'pagination'})
        ul_tag = div_tag.findNext('ul')
        max_pages = 1
        for li_tag in ul_tag.findAll('li'):
            if li_tag.text.isnumeric():
                max_pages = int(li_tag.text)
        return max_pages

    def scrape(self):
        index = 0
        while index < self.find_max_iteration():
            driver = self.selenium_url_maker(urljoin(self.url, self.specific_page_url(index)))
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'vacancy-card'))
            )
            try:
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                for div_tag in soup.findAll('div', {'class': 'vacancy-card'}):
                    link = urljoin(self.url, div_tag.findNext('a', {'class': 'vacancy-card__left'})['href'])
                    title = div_tag.findNext('h3', {'class': 'vacancy-card__title'}).text
                    location = div_tag.findNext('span', {'class': 'vacancy-card__tag'}).text
                    self.positions.append(
                        self.Position(
                            link=link,
                            title=title,
                            location=location
                        )
                    )
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                index += 1
                driver.quit()


