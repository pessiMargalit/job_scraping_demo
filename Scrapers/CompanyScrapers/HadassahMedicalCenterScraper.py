from urllib.parse import urljoin
from Scrapers.Scraper import *


class HadassahMedicalCenterScraper(Scraper):
    name = 'Hadassah Medical Center'
    url = 'https://www.hadassah.org.il/careers/'
    # location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        list_jobs = soup.find('ul', {'class': 'general-container-wide_list'})
        for tag_li in list_jobs.findAll('li'):
            title = tag_li.find('h2', {'class': 'general-container_title'}).text
            link = tag_li.find('a')['href']
            self.positions.append(self.Position(
                title=title.strip(),
                link=urljoin(self.url, link),
                location=self.location
            ))
HadassahMedicalCenterScraper().check_self()