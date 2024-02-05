from urllib.parse import urljoin

import requests

from Scrapers.Scraper import *


class GovernmentScraper(Scraper):
    name = 'Government'
    url = 'https://www.gov.il/he/Search?query=%D7%93%D7%A8%D7%95%D7%A9%D7%99%D7%9D&mainTypes=drushim'

    @staticmethod
    def get_num_of_jobs(url):
        res = requests.get(url)
        return json.loads(res.content)["Total"]

    def get_location(self, job_url):
        base_url = "https://www.gov.il/he/Departments/publications/drushim/"
        index = job_url.find("publications/drushim/")
        extracted_url = job_url[index + len("publications/drushim/"):]
        soup = self.scraping_unit(urljoin(base_url, extracted_url))
        location = soup.find("span", id="cmd_location_1").text.strip()
        return location

    def scrape(self):
        startPage = 0
        json_url = f"https://searchgov.gov.il/govil/generalsearch//?query=%d7%93%d7%a8%d7%95%d7%a9%d7%99%d7%9d&startPage={startPage}&officeOrUnitID=&mainType=drushim&ab=1"

        total_jobs = self.get_num_of_jobs(json_url)
        for index in range(0, total_jobs, 10):
            startPage += 1
            res = requests.get(json_url)
            jobs = json.loads(res.text)["Results"]
            for job in jobs:
                url = job["Url"]
                title = job["Title"]
                location = self.get_location(url)

                self.positions.append(
                    self.Position(
                        title=title,
                        link=url,
                        location=location
                    )
                )


