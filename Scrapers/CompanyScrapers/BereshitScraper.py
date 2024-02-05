from Scrapers.Scraper import *
from urllib.parse import urljoin, quote


class BereshitScraper(Scraper):
    name = 'בראשית'
    url = f'https://bereshit-hr.co.il/%d7%9c%d7%95%d7%97-%d7%9e%d7%a9%d7%a8%d7%95%d7%aa/'
    location = 'ירושלים'

    def get_fields_urls(self):
        soup = self.scraping_unit(self.url)
        fields_urls = soup.find_all('div', {
            'class': 'elementor-cta__button-wrapper elementor-cta__content-item elementor-content-item'})
        return [url.findPrevious('a')['href'] for url in fields_urls]

    def scrape(self):
        urls = self.get_fields_urls()
        for url in urls:
            soup = self.scraping_unit(url)
            positions = soup.find_all(attrs={'class': "elementor-post__card"})
            for pos in positions:
                title = pos.findNext('h3', {'class': 'elementor-post__title'})
                link = pos.findNext('a')
                content = pos.findNext('p')
                self.positions.append(self.Position(
                    title=title.text.strip(),
                    link=link['href'] if link else self.url,
                    content=content.text.strip() if content else None
                ))
