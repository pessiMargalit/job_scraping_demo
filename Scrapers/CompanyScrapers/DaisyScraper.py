from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class DaisyScraper(Scraper):
    name = 'Daisy'
    url = 'https://www.joindaisy.com/careers'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        careers = WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'positions-section')))
        for career in careers.find_elements(By.CSS_SELECTOR, "a.careers-cms.w-inline-block"):
            link = career.get_attribute('href')
            title = career.find_element(By.TAG_NAME, "h1").text
            location = career.find_element(By.CSS_SELECTOR, "div.category-link.filter-category").text
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location,
            ))


DaisyScraper().check_self()
