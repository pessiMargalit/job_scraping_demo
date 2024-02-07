from Scrapers.Scraper import *


class XnesScraper(Scraper):
    name = 'הפניקס בית השקעות'
    url = 'https://www.xnes.co.il/jobs/'
    location = 'ירושלים'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all(attrs={'class': "panel panel-default"})
        for pos in positions:
            title = pos.findNext('p', {'class': 'heading panel-title'})
            self.positions.append(self.Position(
                title=title.text.strip(),
            ))
