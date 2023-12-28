
from Scrapers.Scraper import *


class BynetScraper(Scraper):
    name = 'Bynet'
    url = 'https://www.bynet.co.il/open-positions/'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div in soup.find('div', {'class': 'row'}):
            title = div.findNext('h3', {'class': 'job-role'})
            location = div.findNext('span', {'class': 'job-location-wrapper'})
            link = div.findNext('a', {'class':'js-open-phone vertical-align-middle position-relative d-inline-block bg-red b-radius p-3 mr-2'})
            print(link


                  )
            # if self.location in location.text:
            #     self.positions.append(self.Position(
            #         title=title.text if title else None,
            #         link=link if link else self.url,
            #         location=location.text if location else None,
            #     ))
BynetScraper().scrape()