from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class MDIHealthScraper(Scraper):
    name = 'MDI Health'
    url = 'https://www.mdihealth.com/home/careers/'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        buttons = driver.find_elements(By.CLASS_NAME, 'elementor-toggle-title')
        for button in buttons:
            print(button)
            button.click()
        # Use selenium to wait for the page to load
            WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'elementor-toggle'))
            )
        # Process the page with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # Find the desired elements using BeautifulSoup
        for div in soup.findAll('div', {'class': 'elementor-tab-content elementor-clearfix elementor-active'}):
            title = div.findNext('a', {"class": "elementor-toggle-title"})
            location = div.findNext('span')
            content = div.findNext('div', {"class": "page"})
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=f"{self.url}",
                location=location.text if location else None,
                content=content.text if content else None
            ))

        # Close the driver when done
        driver.quit()


MDIHealthScraper().check_self()
