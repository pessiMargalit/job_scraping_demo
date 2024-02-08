import re

from Scrapers.Scraper import Scraper


class ReubinofLawyerScraper(Scraper):
    name = "גבריאל ראובינוף - משרד עו''ד"
    url = "https://reubinof.co.il/%d7%a2%d7%91%d7%95%d7%93%d7%94-%d7%91%d7%a8%d7%90%d7%95%d7%91%d7%99%d7%a0%d7%95%d7%a3/"
    location = 'ירושלים'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        pattern = r'elementor-element elementor-element-[a-zA-Z0-9]+ elementor-widget elementor-widget-text-editor'
        positions = soup.find_all('div', class_=re.compile(pattern))

        for pos in positions[0:-3:2]:
            title = pos.findNext('div', {'class': 'elementor-widget-container'})
            link = pos.findNext('a', {'class': 'elementor-button-link elementor-button elementor-size-sm'})
            self.positions.append(self.Position(
                title=title.text.strip(),
                link=link['href'] if link else None,
            ))
