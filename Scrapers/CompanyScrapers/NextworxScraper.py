from urllib.parse import urljoin

from Scrapers.Scraper import *


# problem
class NetworxScraper(Scraper):
    name = 'networx'
    url = 'https://apply.workable.com/networx-1/'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for li_tag in soup.findAll('li', {'class': 'styles--1vo9F'}):
            title = li_tag.findNext('h2', {'class': 'styles--3TJHk'}).text
            link = urljoin(self.url, li_tag.findNext('a')['href'])
            location=li_tag.findNext('span',{'class':'styles--1_T3H'}).text
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))


