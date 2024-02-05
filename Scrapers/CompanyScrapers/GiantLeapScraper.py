from Scrapers.Scraper import *


class GiantLeapScraper(Scraper):
    name = 'GiantLeap'
    url = 'https://www.giantleapsystems.com/careers'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        jobs = soup.find("div", {"data-mesh-id": "comp-lozf1hixinlineContent-gridContainer"})

        for job in jobs.findAllNext("div", {"data-testid": "mesh-container-content"}):
            title = job.findNext("span", {"class": "color_11 wixui-rich-text__text"})
            link = job.findNext("a")
            link = link["href"]
            if title:
                self.positions.append(self.Position(
                    title=title.text,
                    link=link
                ))
