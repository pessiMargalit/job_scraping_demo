from Scrapers.Scraper import *
from bs4 import BeautifulSoup


class InnodataScraper(Scraper):
    name = 'innodata'
    url = 'https://innodata.com/career/'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for ul_tag in soup.findAll('ul', {'class': 'elementor-icon-list-items elementor-inline-items'}):
            title, location = ul_tag.findNext('span', {'class': 'elementor-icon-list-text'}).text.strip().split('-')
            link = self.url
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location.strip()
            ))
