from urllib.parse import urljoin, quote
from Scrapers.Scraper import *


class ShaareZedekScraper(Scraper):
    name = 'Shaare Zedek'
    url = 'https://szmc.hunterhrms.com/'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for job in soup.findAll("div", {"class": "hot-job"}):
            title = job.findNext("h5", {"class": "hot-job-name"})
            path = '/פרטי-משרה/'
            encoded_path = quote(path, safe='/')
            job_code = job.findNext("div", {"class": "info"}).get('job-code')
            query = '?jobcode='+job_code
            link = urljoin(self.url, encoded_path + query)
            self.positions.append(self.Position(
                title=title.text,
                location=self.location,
                link=link
            ))
