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
            link = urljoin("https://www.gov.il/he/departments/publications/drushim/", job["UrlName"])
            res = requests.get(link)
            if res.status_code != 200:
                # it's mata data
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
        return are_open_positions

    @staticmethod
    def get_num_json_pages():
        res = requests.get("https://www.gov.il/he/api/PublicationApi/Index?limit=10&skip=0")
        return json.loads(res.content)["pages"]

    def scrape(self):
        num_of_pages = GovernmentScraper().get_num_json_pages()
        for index in range(1, num_of_pages):
            num = index * 50
            try:
                flag = self.get_jobs(
                    f"https://www.gov.il/he/api/PublicationApi/Index?limit={num}&skip={num - 50}")
                if not flag:
                    # it means that was page with no any open position
                    return
            except:
                continue


GovernmentScraper().check_self()
