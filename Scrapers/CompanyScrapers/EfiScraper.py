from concurrent.futures import ThreadPoolExecutor

from Scrapers.Scraper import *


class EfiScraper(Scraper):
    name = 'Efi'
    url = 'https://phe.tbe.taleo.net/phe03/ats/careers/v2/searchResults?next&rowFrom={}' \
          '&act=search&sortColumn=null&sortOrder=null&currentTime=1706608095791'
    location = 'Jerusalem'

    def scrape_page(self, page):
        all_jobs_response = requests.get(self.url.format(page))
        if all_jobs_response.status_code == 200:
            all_jobs_data = all_jobs_response.json()
            for job in all_jobs_data['response']:
                title = job.findNext('h4', {'class': "oracletaleocwsv2-head-title"})
                link = job.findNext('a', {"class": "viewJobLink"})
                location = job.findNext('div')
                self.positions.append(self.Position(
                    title=title.text.strip() if title else None,
                    link=link["href"] if link else self.url,
                    location=location.text.strip() if location else self.location,
                ))

    def scrape(self):
        num_pages = 50
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.scrape_page, i) for i in range(10, num_pages + 1, 10)]
            for future in futures:
                future.result()
