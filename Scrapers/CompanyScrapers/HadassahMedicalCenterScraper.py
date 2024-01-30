from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
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
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.google.com/"}
        req = Request(self.url, headers=headers)
        page = urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        list_jobs = soup.find('ul', {'class': 'general-container-wide_list'})

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.process_job, tag_li) for tag_li in list_jobs.findAll('li')]
        for future in futures:
            result = future.result()
            self.positions.append(result)


HadassahMedicalCenterScraper().check_self()