from Scrapers.Scraper import *


class GreenhouseScraper(Scraper):
    url = "https://api.greenhouse.io/v1/boards/{}/embed/jobs"
    name = 'Greenhouse'

    def scrape(self):
        response = requests.get(self.url)
        response_json = response.json()
        for job in response_json.get('jobs'):
            self.positions.append(
                self.Position(
                    title=job['title'].strip(),
                    link=job['absolute_url'].strip(),
                    location=job['location']['name'].strip()
                )
            )

