from Scrapers.Scraper import *


class ArmoScraper(Scraper):
    name = 'Armo'
    url = 'https://www.armosec.io/careers/'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        i = 1
        for div in soup.findAll('div', {'class': 'position-item'}):
            title = div.findNext('p', {'class': 'position-title'})
            location = div.findNext('p', {'class': 'position-title'})
            link = div.findNext('a', {'class': 'position_link'})
            link = link['href']
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=link if link else self.url,
                #todo: check what to do if the location is part of the title
                location=location.text.strip() if location else None,
            ))


ArmoScraper().check_self()
