from Scrapers.Scraper import *


class OrcaScraper(Scraper):
    name = 'orca'
    url = 'https://orca.security/about/careers/#open-positions'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for li_tag in soup.findAll('li', {'class': 'greenhouse-jobs__position'}):
            title = li_tag.findNext('div', {'class': 'greenhouse-jobs__position-name'}).text
            link = li_tag.findNext('a')['href']
            location = li_tag['data-location']
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))


