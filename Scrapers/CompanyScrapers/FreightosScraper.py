from Scrapers.Scraper import *
from selenium import webdriver

TIMEOUT_IN_SECONDS = 60


class FreightosScraper(Scraper):
    name = 'freightos'
    url = 'https://www.freightos.com/careers/'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'freightos-positions'))
        )
        # # Use BeautifulSoup to parse the driver.page_source
        # # soup = BeautifulSoup(driver.page_source, 'html.parser')
        # show_more_button = WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, 'button'))
        # )
        # show_more_button = driver.find_element(By.CLASS_NAME, 'button')
        # driver.execute_script("arguments[0].scrollIntoView(true);", show_more_button)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        for div in soup.findAll('div', {'class': 'freightos-position-wrap'}):
            title = div.findNext('div', {'class': 'freightos-position-col freightos-position-name'})
            location = div.findNext('span', {'class': 'position-attr'})
            link = div.findNext('a')
            link = link['href']
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=link if link else self.url,
                location=location.text.strip() if location else None,
            ))
        driver.quit()


