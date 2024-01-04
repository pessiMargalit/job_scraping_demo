from enum import Enum

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class JobsDivisionBy(Enum):
    LOCATION = 1
    SUBJECT = 2


class ComeetScraper(Scraper):
    url = ''
    name = ''

    def __init__(self):
        super().__init__()
        self.driver = self.selenium_url_maker(self.url)

    @staticmethod
    def find_location(position, jobs_division_by):
        if jobs_division_by is None:
            return None
        location = None
        if jobs_division_by == JobsDivisionBy.LOCATION:
            career_card = position.find_element(By.XPATH, '../..')
            location = career_card.find_element(By.CSS_SELECTOR, 'h4.positionsGroupTitle').text
        elif jobs_division_by == JobsDivisionBy.SUBJECT:
            xpath_expression = './/li[contains(i/@class, "fa fa-map-marker")]'
            location = position.find_element(By.XPATH, xpath_expression).text
        return location

    def find_division(self):
        xpath = '//div[@ng-controller="CareerCompanyCtrl"]'
        container = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        first_child_element = container.find_element(By.XPATH, './*')
        class_name = first_child_element.get_attribute("class")
        jobs_division_by = None
        if class_name == "container animated fadeIn":
            jobs_division_by = JobsDivisionBy.SUBJECT
        elif class_name == "careerHeroHeader headerContainsLogo":
            jobs_division_by = JobsDivisionBy.LOCATION
        return jobs_division_by

    def scrape(self):
        positions_list = WebDriverWait(self.driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.positionItem')))
        for position in positions_list:
            link = position.get_attribute('href')
            title = position.find_element(By.CSS_SELECTOR, 'h4.positionLink').text
            location = self.find_location(position, self.find_division())
            self.positions.append(self.Position(
                title=title,
                location=location,
                link=link
            ))
