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
        # time out exception
        # btn = WebDriverWait(driver, 12).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, 'jtable-page-number-next-mobile ui-button ui-state-default')))
        # btn.click()
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


# from Scrapers.Scraper import *
# from selenium.webdriver.support import expected_conditions as EC
# TIMEOUT_IN_SECONDS = 10
#
# # does not work
# class ClarivateScraper(Scraper):
#     name = 'clarivate'
#     url = 'https://careers.clarivate.com/search/searchjobs'
#     location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'
#
#     def scrape(self):
#         driver = self.selenium_url_maker(self.url)
#         buttons = driver.find_elements(By.CLASS_NAME, 'elementor-toggle-item')
#
#         for button in buttons:
#             button.click()
#
#             # Wait for the page to load after clicking the button
#             WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, 'elementor-toggle-item'))
#             )
#
#         # Process the page with BeautifulSoup
#         soup = BeautifulSoup(driver.page_source, 'html.parser')
#         # Find the desired elements using BeautifulSoup
#         for div in soup.findAll('div', {'class': 'elementor-tab-content elementor-clearfix elementor-active'}):
#             print(div)
#             title = div.find_next('a', {"class": "elementor-toggle-title"})
#             location = div.find('span')
#             # content = div.find_next('div', {"class": "page"})
#             content = [p.find_next('p').text for p in div]
#             self.positions.append(self.Position(
#                 title=title.text if title else None,
#                 link=f"{self.url}",
#                 location=location.text if location else None,
#                 content=' '.join(content) if content else None
#             ))
#
#         # Close the driver when done
#         driver.quit()
#
#
