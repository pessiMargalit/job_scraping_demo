from Scrapers.Scraper import *


class BlimeyScraper(Scraper):
    url = 'http://theholycity.blimey.tv/index.php/jobs/'
    name = 'Blimey'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, HTML_PARSER)
        for position in soup.findAll('h4'):
            title = position.text
            if 'Jerusalem' in title:
                title = position.text.split('Jerusalem')[1]
            self.positions.append(
                self.Position(
                    title=title
                )
            )
