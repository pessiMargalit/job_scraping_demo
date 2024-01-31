from urllib.parse import urljoin
from Scrapers.Scraper import *


class ShaareZedekScraper(Scraper):
    name = 'Shaare Zedek'
    url = 'https://szmc.hunterhrms.com/'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for job in soup.findAll("div", {"class": "hot-job"}):
            title = job.findNext("h5", {"class": "hot-job-name"})
            link = urljoin(self.url,'/פרטי-משרה/?jobcode=JB-2234')
            self.positions.append(self.Position(
                title=title.text,
                location=self.location,
                link=link
            ))

ShaareZedekScraper().check_self()