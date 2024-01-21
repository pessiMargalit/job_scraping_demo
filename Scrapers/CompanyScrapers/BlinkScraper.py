from Scrapers.Scraper import *


class BlinkScraper(Scraper):
    name = 'Blink'
    url = 'https://www.joinblink.com/careers'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for div_tag in soup.findAll('li', {'class': 'whr-item'}):
            all_title = div_tag.findNext('h3', {'class': 'whr-title'})
            title = all_title.text
            link = all_title.findNext('a')['href']
            location = all_title.findNext('li', {'class': 'whr-location'}).text
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))
