import concurrent.futures
from Scrapers.Scraper import *


class MeuhedetScraper(Scraper):
    name = 'מאוחדת'
    base_url = "https://www.meuhedet.co.il/"
    url = f'{base_url}search?mod=400'
    location = 'Jerusalem'
    pages_num = None

    def __init__(self):
        super().__init__()
        # Get the first jobs page to get the total number of jobs
        self.scrape_page(0)

    def get_careers_json(self, page_number):
        url = "https://hcpgnf9t5w-1.algolianet.com/1/indexes/*/queries"

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "324",
            "Host": "hcpgnf9t5w-1.algolianet.com",
            "Origin": "https://www.meuhedet.co.il",
            "Pragma": "no-cache",
            "Referer": "https://www.meuhedet.co.il/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        }

        query_params = {
            "x-algolia-agent": "Algolia for JavaScript (4.14.2); Browser (lite)",
            "x-algolia-api-key": "0cd884fd17bbf3fb3cf348fcd50dbe8b",
            "x-algolia-application-id": "HCPGNF9T5W"
        }

        payload = {
            "requests": [{
                "indexName": "prod_jobs",
                "params": f"maxValuesPerFacet=1000&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais"
                          "-highlight__&page=" + str(page_number) + "&tagFilters=%5B%5B%22602_37%22%5D%5D&filters"
                                                                    "=ContentRating%3APublic&facets=%5B%22GeoArea%22"
                                                                    "%2C%22City%22%2C%22Specialization%22%2C"
                                                                    "%22JobNumber%22%2C%22JobDescription%22%5D"
            }]
        }

        # Send the POST request
        response = requests.post(url, headers=headers, params=query_params, json=payload)

        if response.status_code == 200:
            try:
                json_result = response.json()
                if not self.pages_num:
                    self.pages_num = json_result["results"][0]["nbHits"]
                return json_result["results"][0]["hits"]
            except ValueError as e:
                print(f"Error parsing JSON from {url}: {e}")
        else:
            print(f"Error fetching data from {url}. Status code: {response.status_code}")
        return []

    def scrape_page(self, page_number):
        jobs = self.get_careers_json(page_number)
        for job in jobs:
            title = job['Description']
            location = job["OrderAreaName"]
            job_id = job["Id"]
            link = f"{self.base_url}jobs/{job_id}/"
            self.positions.append(self.Position(
                title=title,
                location=location,
                link=link
            ))

    def scrape(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            pages = range(1, int(self.pages_num / 20) + 1)
            executor.map(self.scrape_page, pages)
