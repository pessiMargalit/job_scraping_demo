from urllib.error import URLError

from Scrapers.Scraper import *


class SakuraScraper(Scraper):
    name = 'Sakura'
    url = 'https://career.sakura.eu/https://career.sakura.eu/'
    location = 'West Jerusalem'

    def scrape(self):
        try:
            soup = self.scraping_unit(self.url)
            for a_tag in soup.findAll('a', {'class': 'sc-6exb5d-1 eMRVfK'}):
                title = a_tag.text
                link = a_tag['href']
                location = a_tag.find_next('span', {'class': 'sc-6exb5d-4 fUNgrk'}).text
                # should be added only if the location is jerusalem
                self.positions.append(self.Position(
                    title=title,
                    link=link,
                    location=location
                ))
        except URLError as e:
            print(f"Error: {e}")


