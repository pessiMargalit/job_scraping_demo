from urllib.parse import urljoin

from bs4 import BeautifulSoup

from Scrapers.Scraper import Scraper


class PagimatafScraper(Scraper):
    name = "pagimataf"
    url = "https://www.fibi.co.il/wps/portal/FibiMenu/Marketing/Private/General/About/Jobs/JobsMataf/"
    location = "unmentioned"

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for li_tag in soup.findAll('li', {'class': 'articleBody'}):
            title = li_tag.findNext('h3').text.strip()
            link = urljoin(self.url, '#' + li_tag.findNext('div')['id'])
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=self.location
            ))