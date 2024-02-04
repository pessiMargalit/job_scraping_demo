from Scrapers.Scraper import *


class OlivierScraper(Scraper):
    name = 'אוליבייה'
    url = 'https://olivier-il.com/%d7%93%d7%a8%d7%95%d7%a9%d7%99%d7%9d/'
    location = 'ירושלים'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all('div', {'class': 'elementor-post__text'})
        for pos in positions:
            title = pos.findNext('h3', {'class': 'elementor-post__title'})
            link = pos.findNext('a')
            content = pos.findNext('div', {'class': 'elementor-post__excerpt'})
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
                link=link['href'] if link else self.url,
                content=content.text.strip() if content else None
            ))
