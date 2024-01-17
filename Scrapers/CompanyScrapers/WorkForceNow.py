from Scrapers.Scraper import *
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class WorkForceNowScraper(Scraper):
    name = 'workforcenow'
    url = 'https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?cid=4b698d9a-5faa-4fd2-a086-272381a12e04&ccId=19000101_000001&type=MP&lang=en_US'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, 6).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,'current-openings-item')))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for div_tag in soup.findAll('div', {'class': 'current-openings-list'}):
            print(div_tag)
        # self.positions.append(self.Position(
        #     title=title,
        #     link=link,
        #     content=description
        # ))


WorkForceNowScraper().check_self()
