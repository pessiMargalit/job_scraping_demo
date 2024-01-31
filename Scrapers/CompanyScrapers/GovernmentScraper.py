from Scrapers.Scraper import *


class GovernmentScraper(Scraper):
    name = 'Government'
    url = 'https://www.gov.il/he/Search?query=%D7%93%D7%A8%D7%95%D7%A9%D7%99%D7%9D&mainTypes=drushim'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'xs-mb-25 lg-mb-30'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup)
        # jobs = soup.findAll("div", class_="class="xs-mb-25 lg-mb-30"")
        # print(len(jobs))


GovernmentScraper().check_self()
