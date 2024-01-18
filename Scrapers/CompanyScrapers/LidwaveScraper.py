from Scrapers.Scraper import *


class LidwaveScraper(Scraper):
    name = 'Lidware'
    url = 'https://www.lidwave.com/career/'
    location = 'Wst Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('a', {'class': 'space-between'}):
            link = a_tag['href']
            title = a_tag.findNext('h4', {'class', 'book'}).text
            location = a_tag.findNext('p', {'class': 'body book'}).text
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))


