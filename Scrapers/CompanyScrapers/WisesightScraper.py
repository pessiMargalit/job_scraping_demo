from urllib.parse import urljoin
from bs4 import BeautifulSoup

from Scrapers.Scraper import Scraper


class WisesightScraper(Scraper):
    name = 'Wisesight'
    url = 'https://www.careers-page.com/wisesight'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for div_tag in soup.findAll('div', {'class': 'media-body'}):
            title = div_tag.findNext('h5', {'class': 'mt-0 mb-1 primary-color'}).text
            link = div_tag.findNext('a')['href']
            location = div_tag.find('span', {'style': 'margin-right: 10px;'})
            self.positions.append(self.Position(
                title=title,
                link=urljoin(self.url, link),
                location=location.text if location else self.location
            ))
        driver.quit()


