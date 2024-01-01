from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Scrapers.Scraper import *


class PaneraTechScraper(Scraper):
    name = "PaneraTech"
    url = 'https://paneratech.com/careers/current-job-openings/'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        TIMEOUT_IN_SECONDS = 5
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'whr-item'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        careers = soup.find_all('li', class_='whr-item')
        for job in careers:
            link = job.findNext('a')['href']
            title = job.findNext('a').text.strip()
            location = job.findNext('li', class_='whr-location').text.strip()
            prefix = "Location: "
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location[len(prefix):]
            ))
