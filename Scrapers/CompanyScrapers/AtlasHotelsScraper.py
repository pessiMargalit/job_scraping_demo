from Scrapers.Scraper import *


class AtlasHotelsScraper(Scraper):
    url = 'https://www.atlas.co.il/careers/'
    name = 'Atlas'
    location = 'כל הארץ'

    def __init__(self):
        super(AtlasHotelsScraper, self).__init__()

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div in soup.find_all('div', {"class": 'job-card'}):
            title = div.findNext('h3', {'class': 'job-title'})
            link = div.findNext('a', {'class': 'btn btn-secondary job-link'})['href']
            self.positions.append(self.Position(
                title=title.text.strip(),
                link=link
            ))
