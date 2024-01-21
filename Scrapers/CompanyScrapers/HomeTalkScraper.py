from Scrapers.Scraper import *


class HomeTalkScraper(Scraper):
    name = 'Home talk'
    url = 'https://www.careers.hometalk.com/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        i = 1
        for div in soup.findAll('div', {'data-testid': 'container-bg'}):
            title = div.findNext('span', {'class': 'wixui-rich-text__text'})
            location = div.findNext('h1', {'class': 'font_0 wixui-rich-text__text'})
            link = div.findNext('a', {'data-testid': 'linkElement'})
            link = link['href']
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=link if link else self.url,
                location=location.text.strip() if location else None,
            ))


