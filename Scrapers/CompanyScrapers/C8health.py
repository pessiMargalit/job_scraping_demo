from Scrapers.Scraper import *


class C8HealthScraper(Scraper):
    name = 'c8health'
    url = 'https://c8health.com/careers/'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {
            'class': 'col content-box-wrapper content-wrapper-background link-area-box link-type-text content-icon-wrapper-yes icon-hover-animation-fade'}):
            title = div_tag.find_next('div', {'class': 'heading icon-left'}).text
            content = div_tag.find_next('div', {'class': 'content-container'}).text
            link = div_tag['data-link']
            self.positions.append(self.Position(
                title=title,
                link=link,
                content=content
            ))
