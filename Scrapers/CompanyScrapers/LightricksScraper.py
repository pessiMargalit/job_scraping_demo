from Scrapers.Scraper import *


class LightricksScraper(Scraper):
    name = 'Lightricks'
    url = 'https://careers.lightricks.com/careers'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('a', {'list_js_id': 'list_js_id'}):
            h2_tag = a_tag.findNext('h2')
            location = a_tag.findNext('div', {'class': 'job_pagelist_meta list_js_office'})
            self.positions.append(self.Position(
                title=h2_tag.text,
                link=a_tag.findNext('href'),
                location=location
            ))


