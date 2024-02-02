from Scrapers.Scraper import Scraper


class GmedScraper(Scraper):
    name = 'G-Med'
    url = 'https://www.g-med.info/careers'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        page = soup.find('div', {'data-mesh-id': 'comp-jyfvi7mbinlineContent-gridContainer'})
        for div_tag in page.findAll('div', {'data-testid': 'inline-content'}):
            title = div_tag.findNext('span', {'style': 'font-weight:bold;'})
            self.positions.append(self.Position(
                title=title.text,
                link=self.url
            ))


