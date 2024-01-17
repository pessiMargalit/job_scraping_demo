from Scrapers.Scraper import *

from bs4 import BeautifulSoup


class NovamedScraper(Scraper):
    name = 'Novamed'
    url = 'https://www.novamedcorp.com/careers/job-postings/'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)

        for h2_tag in soup.findAll('h2', {"class":"wp-block-heading"}):
            title = h2_tag.text

            if title:
                self.positions.append(self.Position(
                    title=title,
                    link=self.url

                ))


