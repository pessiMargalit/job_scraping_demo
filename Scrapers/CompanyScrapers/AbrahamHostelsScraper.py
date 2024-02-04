from Scrapers.Scraper import *


class AbrahamHostelsScraper(Scraper):
    name = 'Abraham Hostels'
    url = 'https://www.jobs.abraham.travel/work-heb'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all(
            attrs={'data-mesh-id': "comp-jv8bngwf__ebe352bd-20a0-4260-981d-716ef98f24c8inlineContent-gridContainer"})
        for pos in positions:
            title = pos.findNext('span', {'class': 'wixui-rich-text__text'})
            link = pos.findNext('a')
            self.positions.append(self.Position(
                title=title.text,
                link=link['href'] if link else self.url
            ))
