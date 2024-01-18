from Scrapers.Scraper import *


class GenetikaScraper(Scraper):
    name = 'Genetika+'
    url = 'https://www.genetikaplus.com/careers#Open-Positions'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        div_jobs_container = soup.find('div', {'class': 'positions_list w-dyn-items'})
        for div_tag in div_jobs_container.findAll('div', {'class': 'w-dyn-item'}):
            link = div_tag.findNext('a', {'class': 'positions_item w-inline-block'})['href']
            title = div_tag.findNext('h3', {'class': 'heading-style-h6'}).text
            location = div_tag.findNext('div', {'class': 'text-size-xxsmall text-weight-xbold text-style-allcaps'}).text
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))
