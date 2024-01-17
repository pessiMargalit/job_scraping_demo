from Scrapers.Scraper import *


class MobileyeScraper(Scraper):
    name = 'Mobileye'
    url = 'https://careers.mobileye.com/jobs'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('a', {'class': 'card'}):
            h3_tag = a_tag.findNext('h3')
            location = a_tag.findNext('div', {'class': 'location'})
            self.positions.append(self.Position(
                title=h3_tag.text,
                link=a_tag['href'],
                location=location.text
            ))


