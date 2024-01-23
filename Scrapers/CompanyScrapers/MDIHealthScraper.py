from Scrapers.Scraper import *


class MDIHealthScraper(Scraper):
    name = 'MDI Health'
    url = 'https://www.mdihealth.com/home/careers/'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div in soup.findAll('div', {'class': 'elementor-toggle-item'}):
            title = div.findNext('a', {"class": "elementor-toggle-title"})
            location = div.findNext('span')
            content = div.findNext('div', {"class": "page"})
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=self.url,
                location=location.text.strip() if location else None,
                content=content.text.strip() if content else None
            ))
