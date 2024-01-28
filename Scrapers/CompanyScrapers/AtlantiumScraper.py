from Scrapers.Scraper import *


class AtlantiumScraper(Scraper):
    name = 'atlantium'
    url = 'https://atlantium.com/career/https://atlantium.com/career/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
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
