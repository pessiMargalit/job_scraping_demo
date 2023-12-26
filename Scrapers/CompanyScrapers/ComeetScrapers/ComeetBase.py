from enum import Enum

TIMEOUT_IN_SECONDS = 10

from Scrapers.Scraper import *


class JobsDivisionBy(Enum):
    LOCATION = 1
    SUBJECT = 2


class ComeetScraper(Scraper):
    url = ''
    name = ''

    @staticmethod
    def find_location(position, jobs_division_by):
        location = None
        if jobs_division_by == JobsDivisionBy.LOCATION:
            career_card = position.find_element(By.XPATH, '../..')
            location = career_card.find_element(By.CSS_SELECTOR, 'h4.positionsGroupTitle').text
        elif jobs_division_by == JobsDivisionBy.SUBJECT:
            xpath_expression = './/li[contains(i/@class, "fa fa-map-marker")]'
            location = position.find_element(By.XPATH, xpath_expression).text
        return location

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        positions_list = WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.positionItem')))
        for position in positions_list:
            link = position.get_attribute('href')
            title = position.find_element(By.CSS_SELECTOR, 'h4.positionLink').text
            location = ComeetScraper().find_location(position, JobsDivisionBy.LOCATION)
            self.positions.append(self.Position(
                title=title,
                location=location,
                link=link
            ))

