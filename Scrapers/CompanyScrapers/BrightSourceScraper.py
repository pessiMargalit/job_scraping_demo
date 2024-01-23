from Scrapers.Scraper import *


class BrightSourceScraper(Scraper):
    name = 'BrightSource'
    url = 'https://www.newbrightsource.com/careers'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for dcaree in soup.findAll('div', {'class': 'KcpHeO tz5f0K comp-l10svr3o wixui-rich-text'}):
            text = dcaree.findNext('span').text
            text = text.split(",")
            title = text[0]
            location = text[1]
            link = dcaree.findNext('a')
            self.positions.append(self.Position(
                title=title.strip(),
                link=link['href'],
                location=location.strip()
            ))
