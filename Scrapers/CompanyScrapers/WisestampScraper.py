from Scrapers.Scraper import *


# problematic site
class WisestampScraper(Scraper):
    name = 'Wisestamp'
    url = 'https://www.wisestamp.com/careers/'
    location = 'West Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'section-wrapper transparent'}):
            title = div_tag.findNext('h4', {'class': 'wp-block-heading'})
            location = div_tag.findNext('h6', {'class': 'wp-block-heading'})
            link = div_tag.findNext('p').findNext('p').findNext('a')['href']
            # the title class and the location class are not unique
            if title and location and (self.url in link.lower()):
                title = title.text
                location = location.text
                self.positions.append(self.Position(
                    title=title,
                    link=link,
                    location=location
                ))


