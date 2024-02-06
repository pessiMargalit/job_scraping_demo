from urllib.parse import urljoin

from Scrapers.Scraper import *

NUM_OF_JOBS_IN_JSON = 50


class GovernmentScraper(Scraper):
    name = 'Government'
    url = 'https://www.gov.il/he/departments/publications/?limit=10'

    def get_jobs(self, url):
        # are_open_positions = False
        res = requests.get(url)
        if not res.ok:
            return # are_open_positions
        result = json.loads(res.content)["results"]
        for job in result:
            last_date = job["LastDate"]
            given_date = datetime.strptime(last_date, "%Y-%m-%dT%H:%M:%SZ")
            current_date = datetime.utcnow()
            if given_date < current_date:
                continue
            link = urljoin("https://www.gov.il/he/departments/publications/drushim/", job["UrlName"])
            res = requests.get(link)
            if not res.ok:
                # it's mata data , not a position
                continue
            if job["OfficeDesc"]:
                company = job["OfficeDesc"][0]
            else:
                company = None
            title = job["Title"]
            if job["CitiesDesc"]:
                location = job["CitiesDesc"][0]
            else:
                location = None
            self.positions.append(
                self.Position(
                    title=title.strip(),
                    link=link,
                    location=location,
                    company=company if company else self.name
                )
            )
            are_open_positions = True
        # return are_open_positions

    @staticmethod
    def get_num_json_pages():
        res = requests.get(f"https://www.gov.il/he/api/PublicationApi/Index?limit={NUM_OF_JOBS_IN_JSON}0&skip=0")
        return json.loads(res.content)["pages"]

    def scrape(self):
        num_of_pages = GovernmentScraper().get_num_json_pages()
        for index in range(1, num_of_pages):
            num = index * NUM_OF_JOBS_IN_JSON
            # flag = \
            self.get_jobs(
                f"https://www.gov.il/he/api/PublicationApi/Index?limit={num}&skip={num - 50}")
            # if not flag:
            #     # it means that was page with no any open position
            #     return


# GovernmentScraper().check_self()