from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from Scrapers.Scraper import *


class HadassahMedicalCenterScraper(Scraper):
    name = 'Hadassah Medical Center'
    url = 'https://www.hadassah.org.il/careers/'

    def process_job(self, tag_li):
        title = tag_li.find('h2', {'class': 'general-container_title'}).text
        link = tag_li.find('a')['href']
        return self.Position(
            title=title.strip(),
            link=urljoin(self.url, link),
            location=self.location
        )

    def scrape(self):
        soup = self.scraping_unit(self.url)
        list_jobs = soup.find('ul', {'class': 'general-container-wide_list'})

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.process_job, tag_li) for tag_li in list_jobs.findAll('li')]
            for future in futures:
                result = future.result()
                self.positions.append(result)
