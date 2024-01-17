from selenium.webdriver.support import expected_conditions as EC

from Scrapers.Scraper import *


class La2xScraper(Scraper):
    name = 'La2x'
    url = 'https://www.l2x.tech/careers/'
    location = 'west Jerusalem'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        xpath_expression = f"//a[.//span[text()='See Details']]"
        # instead of taking all items there are duplicated
        a_tags = WebDriverWait(driver, 6).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath_expression)))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for a_tag in soup.findAll('div', {
            'class': 'fusion-column-wrapper fusion-flex-justify-content-flex-start fusion-content-layout-column'}):
            print(a_tag.findNext('h2'))
            # job_url = a_tag.get_attribute('href')
            # driver2 = self.selenium_url_maker(job_url)
            # soup = BeautifulSoup(driver2.page_source, "html.parser")
            # title = soup.find('h1', {'id': 'jobTemplateTitle'}).text
            # location = soup.find('div', {'id': 'adlogic_job_details_job_info'}).contents[2].text
            # self.positions.append(self.Position(
            #     title=title,
            #     link=job_url,
            #     location=location
            # ))
            # driver2.quit()
        driver.quit()


