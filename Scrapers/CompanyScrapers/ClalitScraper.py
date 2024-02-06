import concurrent.futures
from Scrapers.Scraper import *


class ClalitScraper(Scraper):
    name = 'כללית'
    url = "https://jobs.clalitapps.co.il/"
    location = "ירושלים והסביבה"

    @staticmethod
    def get_careers_json():
        url = "https://jobs.clalitapps.co.il/CandidateAPI/api//position/Search/9E6C0368-A39E-4D83-803E-CF2AF0BA28DD"

        payload = {"KeyWords": "", "CategoryId": ["0"], "countryId": 2, "cityId": []}

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            try:
                json_result = response.json()
                return json_result["positions"]
            except ValueError as e:
                print(f"Error parsing JSON from {url}: {e}")
        else:
            print(f"Error fetching data from {url}. Status code: {response.status_code}")
        return []

    def scrape(self):
        jobs = self.get_careers_json()
        for job in jobs:
            title = job['jobTitleText']
            location = job["location"]
            job_id = job["compPositionID"]
            link = f"{self.url}clalit/redmatch-apply/redmatch.apply.html?compPositionID={job_id}/"
            self.positions.append(self.Position(
                title=title.strip(),
                location=location,
                link=link
            ))

