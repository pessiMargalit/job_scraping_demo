from Scrapers.Scraper import *


class LightricksScraper(Scraper):
    name = 'Lightricks'
    url = 'https://careers.lightricks.com/careers'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        """
        Greenhouse.....
        """
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('a', {'list_js_id': 'list_js_id'}):
            h3_tag = a_tag.findNext('h3')
            # location = a_tag.findNext('div', {'class': 'location'})
            location = a_tag.findNext('div', {'class': 'job_pagelist_meta list_js_office'})
            self.positions.append(self.Position(
                title=h3_tag.text,
                link=a_tag.findNext('href'),
                location=location
            ))

LightricksScraper().check_self()
