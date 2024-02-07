from sqlalchemy.sql.elements import conv

from Scrapers.Scraper import *


class GenieScraper(Scraper):
    name = "ג'יני שירותי מחשוב לעסקים"
    url = 'https://www.genie.co.il/jobs/'
    location = 'ירושלים'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all('div', class_=lambda x: x and 'elementor-column elementor-col-33 '
                                                                'elementor-top-column elementor-element' in x)
        for pos in positions:
            title = pos.findNext('h3', {'class': 'elementor-heading-title elementor-size-default'})
            content = pos.findNext('div', class_=lambda x: x and ' elementor-widget elementor-widget-text-editor' in x)
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
                content=content.text.strip() if content else None,
            ))
