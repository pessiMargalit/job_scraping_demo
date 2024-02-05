from Scrapers.Scraper import *


class GoldmanCareScraper(Scraper):
    name = 'Goldman Care'
    base_url = 'http://www.goldmancare.co.il/'
    url = f'{base_url}?CategoryID=216'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all('font', {"class": "size4"})
        for pos in positions:
            position = pos.findAllNext('font', {"color": "darkorange"})
            if len(position) >= 2:
                title = position[0]
                content = position[1]
                link = pos.findNext('a')['href']
                self.positions.append(self.Position(
                    title=title.text if title else title,
                    link=f'{self.base_url}/{link}',
                    content=content.text if content else None
                ))
