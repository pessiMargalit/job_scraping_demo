from Scrapers.Scraper import *

from bs4 import BeautifulSoup


class DiagnozmeScraper(Scraper):
    name = 'Diagnoz.me'
    url = 'https://www.news.diagnose.me/careers'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        jobs= soup.find('div', {"class": "c3VDPV sXdULV"})

        for div_tag in jobs.findAll('div', {"class": "gallery-item-container item-container-regular has-custom-focus visible hover-animation-fade-in"}):

            title = div_tag.findNext("p",{"class":"bD0vt9 KNiaIk"}).text
            link= div_tag.findNext('a')['href']
            location= div_tag.findNext("div",{"class":"BOlnTh"}).text


            self.positions.append(self.Position(
                title=title,
                link=link,
                location= location

            ))


