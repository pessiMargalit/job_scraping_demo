from Scrapers.Scraper import *
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class LarsenAndToubroScraper(Scraper):
    name = 'Larsen & Toubro'
    url = 'https://larsentoubrocareers.peoplestrong.com/job/joblist'
    location = 'Jerusalem'

    def scrape(self):
        jobs_json_url = 'https://larsentoubrocareers.peoplestrong.com/api/cp/rest/altone/cp/jobs/v1?offset=0&limit=45'
        for i in range(0, 945, 45):
            jobs_json_url.replace(f'offset={i - 45}', f'offset={i}')
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

