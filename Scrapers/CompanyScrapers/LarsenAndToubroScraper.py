from Scrapers.Scraper import *
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class LarsenAndToubroScraper(Scraper):
    name = 'Larsen & Toubro'
    url = 'https://larsentoubrocareers.peoplestrong.com/job/joblist'
    location = 'Jerusalem'

    def find_requests_url(self, my_format):
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        driver = Scraper.selenium_url_maker(self.url)
        logs = driver.get_log("performance")
        events = [json.loads(log['message'])['message'] for log in logs]
        get_request_ids = []
        for event in events:
            if event['method'] == 'Network.requestWillBeSent':
                if 'request' in event['params']:
                    if event['params']['request']['method'] == 'GET' or event['params']['request']['method'] == 'POST':
                        get_request_ids.append(event['params']['requestId'])
        for event in events:
            if event['method'] == 'Network.responseReceived':
                if 'response' in event['params']:
                    response = event['params']['response']
                    if event['params']['requestId'] in get_request_ids:
                        if my_format in response['mimeType'] and 'jobs' in response['url']:
                            return response['url']

        driver.quit()

    #
    def scrape(self):
        jobs_json_url = self.find_requests_url(my_format='json')
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