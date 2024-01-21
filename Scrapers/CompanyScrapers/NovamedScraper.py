from Scrapers.Scraper import *


class NovamedScraper(Scraper):
    name = 'Novamed'
    url = 'https://www.novamedcorp.com/careers/job-postings/'

    def scrape(self):
        soup = self.scraping_unit(self.url)

        for h2_tag in soup.findAll('h2', {"class": "wp-block-heading"}):
            title = h2_tag.text

            if title:
                self.positions.append(self.Position(
                    title=title,
                    link=self.url

                ))
