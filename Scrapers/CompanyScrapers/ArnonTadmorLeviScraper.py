from urllib.parse import urljoin
from Scrapers.Scraper import *


class ArnonTadmorLeviScraper(Scraper):
    name = 'ארנון, תדמור-לוי'
    url = 'https://arnontl.com/he/'
    location = 'ירושלים'
    professional_fields = ['lawyers', 'admin', 'interns', 'alumni']

    def scrape(self):
        for field in self.professional_fields:
            specific_url = urljoin(self.url, field)
            soup = self.scraping_unit(specific_url)
            positions = soup.find_all('div', {'class': 'accordion-header show'})
            for pos in positions:
                title = pos.findNext('h6', {'class': 'h6-title w-100'})
                content = pos.findNext('div', {'class': 'w-100'})
                self.positions.append(self.Position(
                    title=title.text.strip() if title else None,
                    content=content.text.strip() if content else None,
                    link=specific_url
                ))
