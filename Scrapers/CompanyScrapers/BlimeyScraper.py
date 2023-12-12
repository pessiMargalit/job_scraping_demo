from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class BlimeyScraper(Scraper):
    url = 'http://theholycity.blimey.tv/index.php/jobs/'
    name = 'Blimey'

    def __init__(self):
        super(BlimeyScraper, self).__init__()

    def scrape(self):
        # Use selenium to wait for the page to load
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'entry-content'))
        )
        # Use BeautifulSoup to parse the driver.page_source
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # soup = self.scraping_unit(driver.current_url)
        # Process the page with BeautifulSoup
        for a_tag in soup.findAll('div', {'class': "entry-content"}):
            title = a_tag.find_next('strong')
            content = [p.find_next('p') for p in a_tag]
            self.positions.append(self.Position(
                title=title.text if title else None,
                content=' \n'.join([c.text for c in content if c is not None]) if content else None
            ))
        # Close the driver when done
        driver.quit()


# Run the scraper
BlimeyScraper().check_self(content=True)
