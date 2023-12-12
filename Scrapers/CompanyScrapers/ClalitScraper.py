from Scrapers.Scraper import *

# Constants
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
        # Use BeautifulSoup to parse the driver.page_source
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # soup = self.scraping_unit(driver.current_url)
        # Process the page with BeautifulSoup
        for a_tag in soup.findAll('a', {'class': 'job-item'}):
            title = a_tag.find_next('span', {"data-field": "jobTitleText"})
            location = a_tag.find_next('span', {"data-field": "location"})
            content = a_tag.find_next('div', {"class": "ellipsis-text"})
            # if location is not None and "ירושלים והסביבה" in location.text:
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=f"{self.url}/{a_tag.get('href')}",
                location=location.text if location else None,
                content=content.text if content else None
            ))

        # Close the driver when done
        driver.quit()


# Run the scraper
ClalitScraper().check_self()