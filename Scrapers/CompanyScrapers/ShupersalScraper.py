from urllib.parse import urljoin

from Scrapers.Scraper import *


class ShupersalScraper(Scraper):
    name = 'שופרסל'
    url = "https://career.shufersal.co.il/site/SearchWithParams"

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        load_more = WebDriverWait(driver, 10) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#load_more_btn')))

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        total = int(soup.find("span", {'ng-bind': 'TotalPublishedPositions'}).text.strip())

        for i in range(0, int(total / 5)):
            load_more.click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        jobs = soup.findAll("div", class_="item ng-scope")
        for job in jobs:
            title = job.findNext("div", class_="job ng-binding").text.strip()
            location = job.findNext("div", class_="location ng-binding").text.strip()
            link = urljoin(self.url, job.findNext("a", class_="btn")["href"])

            self.positions.append(
                self.Position(
                    title=title,
                    location=location,
                    link=link
                )
            )
        driver.quit()
