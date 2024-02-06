from urllib.parse import urljoin

from Scrapers.Scraper import *

NUM_OF_JOBS_IN_JSON = 10


class GovernmentScraper(Scraper):
    name = 'Government'
    url = 'https://www.gov.il/he/departments/publications/?limit=10'

    def get_jobs(self, url):
        are_open_positions = False
        res = requests.get(url)
        result = json.loads(res.content)["results"]
        for job in result:
            last_date = job["LastDate"]
            given_date = datetime.strptime(last_date, "%Y-%m-%dT%H:%M:%SZ")
            current_date = datetime.utcnow()
            if given_date < current_date:
                continue
            title = job["Title"]
            link = urljoin("https://www.gov.il/he/departments/publications/drushim/", job["UrlName"])
            if job["CitiesDesc"]:
                location = job["CitiesDesc"][0]
            else:
                location = None
            self.positions.append(
                self.Position(
                    title=title.strip(),
                    link=link,
                    location=location
                )
            )
            are_open_positions = True
        return are_open_positions

    @staticmethod
    def get_num_of_total_jobs():
        res = requests.get(f"https://www.gov.il/he/api/PublicationApi/Index?limit={NUM_OF_JOBS_IN_JSON}&skip=0")
        return json.loads(res.content)["total"]

    def scrape(self):
        num_of_total_jobs = GovernmentScraper().get_num_of_total_jobs()
        for index in range(50, num_of_total_jobs, NUM_OF_JOBS_IN_JSON):
            flag = self.get_jobs(f"https://www.gov.il/he/api/PublicationApi/Index?limit={index}&skip={index - 50}")
            if not flag:
                # its means that was page with no any open position
                return

