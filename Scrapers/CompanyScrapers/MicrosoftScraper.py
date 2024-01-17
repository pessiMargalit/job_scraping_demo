from Scrapers.CompanyScrapers.JsonScrapers.JsonScraper import JsonScraper
import requests
import urllib
import concurrent.futures
from Scrapers.CompanyScrapers.JsonScrapers.JsonScraper import JsonScraper
import requests
import urllib.parse


class MicrosoftScraper(JsonScraper):
    name = 'Microsoft'
    url = "https://gcsservices.careers.microsoft.com/search/api/v1/search"

    def get_careers_json(self):
        # gets from req
        page_number = 1
        json = requests.get(self.url).json()
        num_of_jobs = json["operationResult"]["result"]["totalJobs"]
        while page_number <= (num_of_jobs / 20):
            # every page contain 20 careers
            url = f"{self.url}?pg={page_number}"
            response = requests.get(url)
        if response.status_code == 200:
            try:
                json_result = response.json()
                yield json_result["operationResult"]["result"]["jobs"]
            except ValueError as e:
                print(f"Error parsing JSON from {url}: {e}")
            else:
                print(f"Error fetching data from {url}. Status code: {response.status_code}")
                page_number += 1

    def scrape(self):
        for jobs in MicrosoftScraper().get_careers_json():
            for job in jobs:
                title = job['title']
                location = job["properties"]['primaryLocation']
                content = job['properties']['description']
                job_id = job["jobId"]
                title_no_space = title.replace(" ", "-")
                correct_title = urllib.parse.quote(title_no_space, safe='')
                link = f"https://jobs.careers.microsoft.com/global/en/job/{job_id}/{correct_title}"
                self.positions.append(self.Position(
                    title=title,
                    location=location,
                    content=content,
                    link=link
                ))
    def get_careers_json(self, page_number):
        url = f"{self.url}?pg={page_number}"
        response = requests.get(url)
        if response.status_code == 200:
            try:
                json_result = response.json()
                return json_result["operationResult"]["result"]["jobs"]
            except ValueError as e:
                print(f"Error parsing JSON from {url}: {e}")
        else:
            print(f"Error fetching data from {url}. Status code: {response.status_code}")
        return []

    def scrape_page(self, page_number):
        jobs = self.get_careers_json(page_number)
        for job in jobs:
            title = job['title']
            location = job["properties"]['primaryLocation']
            content = job['properties']['description']
            job_id = job["jobId"]
            title_no_space = title.replace(" ", "-")
            correct_title = urllib.parse.quote(title_no_space, safe='')
            link = f"https://jobs.careers.microsoft.com/global/en/job/{job_id}/{correct_title}"
            self.positions.append(self.Position(
                title=title,
                location=location,
                content=content,
                link=link
            ))

    def scrape(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            num_of_jobs = requests.get(self.url).json()["operationResult"]["result"]["totalJobs"]
            pages = range(1, int(num_of_jobs / 20) + 1)
            executor.map(self.scrape_page, pages)


MicrosoftScraper().check_self()