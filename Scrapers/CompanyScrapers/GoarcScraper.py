from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class GoarcScraper(Scraper):
    url = 'https://go-arc.com/careers/'
    name = 'Goarc'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        a_tags = driver.find_elements(By.CLASS_NAME, 'comeet-position')
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'comeet-position')))
        for a_tag in a_tags:
            job_url = a_tag.get_attribute('href')
            driver2 = self.selenium_url_maker(job_url)
            new_page_soup = BeautifulSoup(driver2.page_source, 'html.parser')
            data = new_page_soup.find('div', {'class': 'comeet-outer-wrapper'})
            title = data.find('h2', {'class': 'comeet-position-name'})
            location = data.find('span', {'class': 'comeet-position-location'})
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=job_url if job_url else self.url,
                location=location.text if location else None,
            ))
            driver2.quit()

        driver.quit()


GoarcScraper().check_self()
