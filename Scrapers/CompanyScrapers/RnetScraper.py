from Scrapers.Scraper import *


class RnetScraper(Scraper):
    name = 'Rnet'
    url = 'https://www.rnet-tech.com/index.php/careers'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers=soup.findAll('h1',attrs={'itemprop':'name'})
        for a_tag in careers:
            title = a_tag.text
            link = a_tag['href']
            self.positions.append(self.Position(
                title=title,
                link=link,
            ))


