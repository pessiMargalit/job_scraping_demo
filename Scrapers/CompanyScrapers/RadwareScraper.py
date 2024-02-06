from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from Scrapers.Scraper import Scraper


class RadwareScraper(Scraper):
    name = 'Radware'
    url = 'https://radware.taleo.net/careersection/ex/joblist.ftl'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('table', {'class': 'contentlist'})
        next_link = driver.find_element(By.ID, 'requisitionListInterface.pagerDivID1822.Next')
        next_link.click()
        for tr_tag in table.findAll('tr', {'id': 'requisitionListInterface.ID3080.row'}):
            if tr_tag:
                title = tr_tag.findNext('span', {'class': 'titlelink'})
                location = tr_tag.findNext('div', {'class': 'morelocation'})

                self.positions.append(self.Position(
                    title=title.text.strip(),
                    location=location.text.strip() if location else None,
                    link=self.url
                ))
        driver.quit()


