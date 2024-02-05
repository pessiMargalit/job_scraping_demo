from urllib.parse import urljoin

from Scrapers.Scraper import *


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
        res = requests.get("https://www.gov.il/he/api/PublicationApi/Index?limit=10&skip=0")
        return json.loads(res.content)["total"]

    def scrape(self):
        num_of_total_jobs = GovernmentScraper().get_num_of_total_jobs()
        for index in range(1, int(num_of_total_jobs / 10)):
            flag = self.get_jobs(f"https://www.gov.il/he/api/PublicationApi/Index?limit={index}0&skip={index + 1}0")
            if not flag:
                # its means that was page with no any open position
                return
