from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class GoarcScraper(Scraper):
    url = 'https://go-arc.com/careers/'
    name = 'Goarc'

    def __init__(self):
        super(GoarcScraper, self).__init__()

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        a_tags = driver.find_elements(By.CLASS_NAME, 'comeet-position')
        for a_tag in a_tags:
            link = a_tag.get_attribute('href')
            a_tag.click()
            WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(EC.url_changes(self.url))
            new_page_soup = BeautifulSoup(driver.page_source, 'html.parser')
            data = new_page_soup.find('div', {'class': 'comeet-outer-wrapper'})
            title = data.findNext('h2', {'class': 'comeet-position-name'})
            location = data.findNext('span', {'class': 'comeet-position-location'})
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=link if link else self.url,
                location=location.text if location else None,
            ))

        driver.quit()


GoarcScraper().scrape()
