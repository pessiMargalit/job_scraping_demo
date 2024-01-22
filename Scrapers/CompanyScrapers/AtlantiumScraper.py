from Scrapers.Scraper import *


class AtlantiumScraper(Scraper):
    name = 'atlantium'
    url = 'https://atlantium.com/career/https://atlantium.com/career/'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for div in soup.findAll('div', {'class': 'panel-heading'}):
            a_href = div.findNext('a')['href']
            title = div.findNext('h4').text
            link = "https://atlantium.com/career/https://atlantium.com/career/" + a_href
            location = None
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))
