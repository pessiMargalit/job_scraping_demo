from urllib.parse import urljoin

from Scrapers.Scraper import Scraper


class AranScraper(Scraper):
    name = 'aran'
    url = 'https://www.aran-rd.com/category/career/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        div_careers = soup.find('div', {'class': 'row'})
        for career in div_careers.findAll('div', {'class': 'entry-content'}):
            title = career.findNext('h2').text.strip()
            email = career.findNext('a')['href']
            self.positions.append(self.Position(
                title=title,
                content=email,
                link=self.url
            ))


AranScraper().check_self()
