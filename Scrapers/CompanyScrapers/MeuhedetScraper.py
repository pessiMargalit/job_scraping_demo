import concurrent.futures
from Scrapers.Scraper import *


class MeuhedetScraper(Scraper):
    name = 'מאוחדת'
    base_url = "https://www.meuhedet.co.il/"
    url = f'{base_url}search?mod=400'
    location = 'ירושלים'
    pages_num = None

    def __init__(self):
        super().__init__()
        # Get the first jobs page to get the total number of jobs
        self.scrape_page(0)

    def get_careers_json(self, page_number):
        url = "https://hcpgnf9t5w-1.algolianet.com/1/indexes/*/queries"

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
        response = requests.post(url, params=query_params, json=payload)

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
                title=title.strip(),
                location=location,
                link=link
            ))

    def scrape(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            pages = range(1, int(self.pages_num / 20) + 1)
            executor.map(self.scrape_page, pages)


