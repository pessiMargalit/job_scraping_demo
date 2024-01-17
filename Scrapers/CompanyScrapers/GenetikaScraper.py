from Scrapers.Scraper import *


class GenetikaScraper(Scraper):
    name = 'Genetika+'
    url = 'https://www.genetikaplus.com/jobs'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {
            'data-mesh-id': 'comp-kus2lyyu1__1536698f-bde9-4514-894e-1f0157e06e97inlineContent-gridContainer'}):
            title = div_tag.findNext('h2', {"class": "font_2 wixui-rich-text__text"}).text
            link = div_tag.findNext('a')['href']
            location = div_tag.findNext('p', {"class": "font_8 wixui-rich-text__text"}).text
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))
