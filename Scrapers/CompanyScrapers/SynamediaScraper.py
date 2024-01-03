from Scrapers.Scraper import *
from urllib.parse import urljoin
TIMEOUT_IN_SECONDS = 60


class SynamediaScraper(Scraper):
    name = 'Synamedia'
    url = 'https://synamedia.sumtotal.host/Careers/search?q='
    location = 'Jerusalem'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'job-data-container'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for div in soup.findAll('div', {'class': 'content'}):
            title = div.findNext('a')
            location = div.findNext('span', {'class': 'form-column word-break'})
            button = div.findNext('button', {'class': 'btn btn-primary'})
            position_number = button['aria-labelledby'][-4:]
            link = f'{self.url[:46]}(slideout:job/{position_number})?q='
            link = urljoin('', link)
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=link if link else self.url,
                location=location.text.strip() if location else None,
            ))


SynamediaScraper().check_self()
