import time
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Scrapers.Scraper import Scraper

TIMEOUT_IN_SECONDS = 10


class WellsenseScraper(Scraper):
    name = 'wellsense'
    url = 'https://www.wellsense.org/careers/jobs'

    def scrape(self):
        driver = Scraper.selenium_url_maker(self.url, debug=True)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.table")))
        next = False
        while (True):
            time.sleep(60)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find("table", {"class": "table b-table table-striped table-hover"})

            for tr_tag in table.find_all('tr', {"role": "row"}):
                title = tr_tag.find_next("a").text
                link = tr_tag.find_next('a')['href']
                location = tr_tag.find_next("td", {"aria-colindex": "3"}).text
                self.positions.append(self.Position(
                    title=title,
                    link=link,
                    location=location
                ))
            buttons = driver.find_elements(By.XPATH,
                                           '//*[@id="hs_cos_wrapper_widget_1661285634857"]/div/div/div[2]/ul/li[7]/button')
            for button in buttons:
                if button.accessible_name == 'Go to next page':
                    button.click()
                    next = True
            if next == False:
                break
            next = False


WellsenseScraper().check_self()
