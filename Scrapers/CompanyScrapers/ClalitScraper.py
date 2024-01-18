from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class ClalitScraper(Scraper):
    name = 'קופת חולים כללית'
    url = 'https://jobs.clalitapps.co.il/clalit/index.html?ci=0'

    def scrape(self):
        # Use selenium to wait for the page to load
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'job-item'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for a_tag in soup.findAll('a', {'class': 'job-item'}):
            title = a_tag.find_next('span', {"data-field": "jobTitleText"})
            location = a_tag.find_next('span', {"data-field": "location"})
            content = a_tag.find_next('div', {"class": "ellipsis-text"})
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=f"{self.url}/{a_tag.get('href')}",
                location=location.text if location else None,
                content=content.text if content else None
            ))

        # Close the driver when done
        driver.quit()

