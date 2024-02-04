from Scrapers.Scraper import *


class OpticalCenterScraper(Scraper):
    name = 'Optical Center'
    url = 'https://www.optical-center.co.il/rejoignez-nous'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        class_name = re.compile(r'opt\d* insLink')
        positions = soup.find_all(
            attrs={'class': class_name})
        pos_num = 0
        for pos in positions:
            pos_num += 1
            title = pos.findNext('span', {'class': 'txt'})
            link = f'{self.url}?inscription={pos_num}'
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
                link=link if link else self.url
            ))
