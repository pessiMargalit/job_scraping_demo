from Scrapers.Scraper import *


class BitanScraper(Scraper):
    name = 'ביתן'
    url = "https://www.ybitan.co.il/web-pages/7"

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[style="font-size:14px"]'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        jobs = soup.findAll("span", style='font-size:14px')
        for job in jobs:
            title = job.findNext("strong").text.strip()
            self.positions.append(
                self.Position(
                    title=title,
                    link=self.url
                )
            )
