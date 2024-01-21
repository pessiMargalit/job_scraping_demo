from Scrapers.Scraper import *
from urllib.parse import urljoin


class FuriouscropScraper(Scraper):
    name = 'Furiouscrop'
    url = 'https://furiouscorp.com/careers/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        data = soup.find('div', {'id': 'furious-israel'})
        ul = data.findNext('ul')
        for li_tag in ul.findAll('li'):
            # the looping throw a_tag was nicer code however it does not work
            link = li_tag.findNext('a')['href']
            if self.url not in link.lower():
                # some of the link contains only partial url without the domain name
                link = urljoin(self.url, link)
            title=li_tag.findNext('a').text
            self.positions.append(self.Position(
                title=title,
                link=link,
            ))


