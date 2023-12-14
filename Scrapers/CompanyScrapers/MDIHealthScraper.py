from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class MDIHealthScraper(Scraper):
    name = 'MDI Health'
    url = 'https://www.mdihealth.com/home/careers/'
    location = 'Jerusalem'  # default location, when not set it's automatically 'Jerusalem'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        buttons = driver.find_elements(By.CLASS_NAME, 'elementor-toggle-item')

        for button in buttons:
            button.click()

            # Wait for the page to load after clicking the button
            WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'elementor-toggle-item'))
            )

        # Process the page with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # Find the desired elements using BeautifulSoup
        for div in soup.findAll('div', {'class': 'elementor-tab-content elementor-clearfix elementor-active'}):
            title = div.find_next('a', {"class": "elementor-toggle-title"})
            location = div.find('span')
            # content = div.find_next('div', {"class": "page"})
            content = [p.find_next('p').text for p in div]
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=f"{self.url}",
                location=location.text if location else None,
                content=' '.join(content) if content else None
            ))

        # Close the driver when done
        driver.quit()


# Run the scraper
MDIHealthScraper().check_self(content=True)
