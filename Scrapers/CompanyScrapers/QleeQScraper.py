from Scrapers.Scraper import *

from bs4 import BeautifulSoup


class QleeQScraper(Scraper):
    name = 'QleeQ'
    url = 'https://qleeq.azurewebsites.net/careers.html'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        jobs= soup.find('div', {"class": "box"})
        for p_tag in jobs.findAll('p'):
            t = p_tag.findNext("h4")
            title = t.text if t else None
            if title:
                self.positions.append(self.Position(
                    title=title,
                    link=self.url

                ))


