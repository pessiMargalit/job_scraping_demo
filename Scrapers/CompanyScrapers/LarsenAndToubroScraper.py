import concurrent.futures

from Scrapers.Scraper import *


class LarsenAndToubroScraper(Scraper):
    name = 'Larsen & Toubro'
    url = 'https://larsentoubrocareers.peoplestrong.com/job/joblist'
    location = 'Jerusalem'

    def calculate_num_of_positions(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            num_of_positions = soup.find_all(attrs={'class': 'totale-num text-uppercase'})
            return num_of_positions

    def scrape(self):
        # num_of_positions = self.calculate_num_of_positions()
        jobs_json_url = 'https://larsentoubrocareers.peoplestrong.com/api/cp/rest/altone/cp/jobs/v1?offset=0&limit=45'

        # Use a ThreadPoolExecutor to parallelize the scraping process
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []

            for i in range(0, 1000, 45):
                jobs_json_url = jobs_json_url.replace(f'offset={i - 45}', f'offset={i}')

                future = executor.submit(self.scrape_job_data, jobs_json_url)
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
