from Scrapers.Scraper import *


class MDIHealthScraper(Scraper):
    name = 'MDIHealth'
    url = 'https://www.mdihealth.com/home/careers/'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'elementor-tab-title'}):
            title = div_tag.findNext('a', {'class': 'elementor-toggle-title'}).text
            location = div_tag.findNext('p').text
            link = self.url
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))


