from Scrapers.Scraper import *


class AriyeBuildScraper(Scraper):
    name = 'אחוזת אריה'
    url = 'https://www.ariyebuild.co.il/he/home#!92'
    location = 'ירושלים'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all('div', {'id': 'elements_92'})
        for pos in positions:
            title = pos.findNext('h2', {'class': 'project-title'})
            link = pos.findNext('a')
            content = pos.findNext('p', {'class': 'project-subtitle'})
            self.positions.append(self.Position(
                title=title.text.strip(),
                link=link['href'] if link else self.url,
                content=content.text.strip() if content else None
            ))
