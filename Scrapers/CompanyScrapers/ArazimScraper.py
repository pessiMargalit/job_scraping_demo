from Scrapers.Scraper import *


class ArazimScraper(Scraper):
    name = 'Arazim'
    url = 'https://arazim.co.il/careers/'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find("div", {"class": "elementor elementor-339"})

        for pos in positions.findAll("section", {'data-element_type': "section"})[2:-1]:
            title = pos.findNext('h2', {'class': 'elementor-heading-title elementor-size-default'})

            self.positions.append(self.Position(
                title=title.text.strip(),
                link=self.url
            ))
