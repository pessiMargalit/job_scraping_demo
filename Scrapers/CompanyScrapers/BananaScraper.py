from Scrapers.Scraper import *


class BananaScraper(Scraper):
    name = 'בננה'
    url = 'https://www.banana-fashion.co.il/%d7%93%d7%a8%d7%95%d7%a9%d7%99%d7%9d/'
    location = 'ירושלים'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        divs = soup.find_all(attrs={'class': "elementor-text-editor elementor-clearfix"})
        positions = [pos.find_all('p') for pos in divs]
        for pos in positions[0]:
            title_tag = pos.findNext('strong')
            title = title_tag.text.strip()
            content = pos.text.strip()[len(title):]
            self.positions.append(self.Position(
                title=title,
                content=content if content else None
            ))
