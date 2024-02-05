from Scrapers.Scraper import *


class IBIScraper(Scraper):
    name = 'IBI'
    url = 'https://www.ibi.co.il/career/'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.select('div[class*="col-career-post filter-item"]')
        for pos in positions:
            title = pos.findNext('h4', {'class': 'career-title'})
            link = pos.findNext('a')
            self.positions.append(self.Position(
                title=title.text.strip() if title else title,
                link=link['href'] if link else self.url
            ))
