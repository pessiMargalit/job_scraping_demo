import concurrent.futures

from Scrapers.Scraper import *


class LarsenAndToubroScraper(Scraper):
    name = 'Larsen & Toubro'
    url = 'https://larsentoubrocareers.peoplestrong.com/api/cp/rest/altone/cp/jobs/v1?offset=0&limit=100'
    location = 'Jerusalem'

    def get_all_jobs_urls(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            res_json = response.json()
            total = res_json.get('totalRecords')
            urls = [self.url.replace('offset=0', f'offset={i}') for i in range(0, total, 100)]
            return urls

    def scrape(self):

        jobs_urls = self.get_all_jobs_urls()

        # Use a ThreadPoolExecutor to parallelize the scraping process
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []

            for url in jobs_urls:
                future = executor.submit(self.scrape_job_data, url)
                futures.append(future)

            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

    def scrape_job_data(self, jobs_json_url):
        all_jobs_response = requests.get(jobs_json_url)

        if all_jobs_response.status_code == 200:
            all_jobs_data = all_jobs_response.json()
            for job in all_jobs_data['response']:
                title = job['jobTitle']
                location = job['locationHierarchyComplete']
                link = job['jobDetailUrl']
                self.positions.append(self.Position(
                    title=title.strip() if title else None,
                    link=link.strip() if link else self.url,
                    location=location.strip() if location else None,
                ))
