from urllib.parse import urljoin

from Scrapers.Scraper import *


# to continue tomorrow
class DellScraper(Scraper):
    name = 'dell'
    url = 'https://jobs.dell.com/location/israel-jobs/375/294640/2'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        table = soup.find('section', {'id': 'search-results-list'})
        for li_tag in table.findAll('li'):
            a_tag = li_tag.findNext('a')
            link = urljoin(self.url,a_tag['href'])
            title = a_tag.findNext('h2').text.strip()
            location = a_tag.findNext('span', 'job-location-search').text.strip()
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))
