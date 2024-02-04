from urllib.parse import urljoin

from Scrapers.Scraper import Scraper


class AranScraper(Scraper):
    name = 'Aran'
    url = 'https://www.aran-rd.com/category/career/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        div_careers = soup.find('div', {'class': 'row'})
        for career in div_careers.findAll('div', {'class': 'entry-content'}):
            title = career.findNext('h2').text.strip()
            email = career.findNext('a')['href']
            article = career.find_parent('article') if career else None
            article_id = article['id']
            job_link = f"{self.url}#{article_id}" if article_id else self.url
            self.positions.append(self.Position(
                title=title,
                content=email,
                link=job_link
            ))