from Scrapers.Scraper import *


class BDSKScraper(Scraper):
    name = "בן דוד שלוי קופ ושות' רואי חשבון"
    url = 'https://bdsk.co.il/%d7%9e%d7%a9%d7%a8%d7%95%d7%aa/'
    location = 'ירושלים'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all(class_=lambda value: value and ' elementor-section elementor-inner-section '
                                                                 'elementor-element elementor-element-879a8ee '
                                                                 'elementor-section-boxed elementor-section-height'
                                                                 '-default elementor-section-height-default' in value)
        for pos in positions:
            title = pos.findNext('span').text.strip()
            link = pos.findNext('li', {'itemprop': 'datePublished'}).findNext('a')
            content = pos.findNext(attrs={'class': 'ee-unfold__content'})
            location = pos.findPrevious('h2', {'class': 'elementor-heading-title elementor-size-default'})
            self.positions.append(self.Position(
                title=' '.join(title.split()),
                link=link['href'] if link else self.url,
                content=content.text.strip() if content else None,
                location=location.text.strip() if location else self.location
            ))
