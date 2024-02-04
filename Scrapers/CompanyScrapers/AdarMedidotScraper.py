from Scrapers.Scraper import *


class AdarMedidotScraper(Scraper):
    name = 'Adar Medidot'
    url = 'http://www.adarkav.org.il/%d7%94%d7%92%d7%a9%d7%aa-%d7%9e%d7%95%d7%a2%d7%9e%d7%93%d7%95%d7%aa/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for tag_h3 in soup.findAll('h3'):
            tag_a = tag_h3.find('a')
            detail = tag_a.text.split('–')
            title = detail[0]
            location = detail[1]
            link = tag_a['href']
            self.positions.append(self.Position(
                title=title.strip(),
                link=link,
                location=location.strip()
            ))
