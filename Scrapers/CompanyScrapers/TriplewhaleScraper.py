from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class TriplewhaleScraper(Scraper):
    name = 'Triplewhale'
    url = 'https://www.triplewhale.com/careers'

    def scrape(self):
        # driver = self.selenium_url_maker(self.url)
        # WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
        #     EC.presence_of_element_located((By.ID, 'lever-jobs-container'))
        # )
        #
        # # Use BeautifulSoup to parse the driver.page_source
        # soup = BeautifulSoup(driver.page_source, 'html.parser')

        soup = self.scraping_unit(self.url)
        jobs = soup.find_all('div', {'id': "lever-jobs-container"})
        print(jobs)
        for li in soup.find_all('li', {'class': 'lever-job'}):
            career = li.findNext('a', {'class': 'lever-job-title'})
            location = li.findNext('span')
            self.positions.append(self.Position(
                title=career.text if career else None,
                link=career['href'] if career else None,
                location=location.text if location else None
            ))


TriplewhaleScraper().check_self()
