from Scrapers.Scraper import *

from bs4 import BeautifulSoup


class OmnixMedicalScraper(Scraper):
    name = 'Omnix Medical'
    url = 'https://omnixmedical.com/careers/'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        jobs= soup.find("section",{"class":"elementor-widget-wrap elementor-element-populated"})

        for div_tag in jobs.findAll('div', {"class":"elementor-widget-container"}):
            title = div_tag.findNext('h2', {"class": "elementor-heading-title elementor-size-default"}).text
            print(title)
            if title:
                self.positions.append(self.Position(
                    title=title,
                    link=self.url

                ))


OmnixMedicalScraper().check_self()