from Scrapers.Scraper import *

# we have to take the location
class HydroxScraper(Scraper):
    name = 'hydrox'
    url = 'https://hydrox.earth/hydro-x-careers/'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'elementor-post__text'}):
            title = div_tag.find_next('h3')
            link = div_tag.find_next('a')['href']
            self.positions.append(self.Position(
                title=title.text,
                link=link
            ))


