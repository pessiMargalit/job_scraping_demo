from Scrapers.Scraper import *


class SurgimateScraper(Scraper):
    name = 'Surgimate'
    url = 'https://www.surgimate.com/careers'
    location = 'West Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('a', {'class': 'comeet-position'}):
            link = a_tag['href']
            title = a_tag.findNext('div', {'class': 'comeet-position-name'}).text
            job_meta_data = a_tag.findNext('div', {'class': 'comeet-position-meta'}).text
            location = job_meta_data.split()[0]
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))


