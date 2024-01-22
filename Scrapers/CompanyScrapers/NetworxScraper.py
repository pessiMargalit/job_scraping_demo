from urllib.parse import urljoin

from Scrapers.Scraper import *


class NetworxScraper(Scraper):
    name = 'networx'
    url = 'https://apply.workable.com/networx-1/'

    def scrape(self):
        response = requests.get('https://apply.workable.com/api/v3/accounts/networx-1/jobs')
        jobs_json = response.json().get('results')
        for job in jobs_json:
            self.positions.append(
                self.Position(
                    title=job.get('title'),
                    link=f"https://apply.workable.com/{self.slug}/j/{job.get('shortcode')}/",
                    location=f"{job.get('location').get('country')}, {job.get('location').get('city')}",
                    remote=job.get('remote')
                )
            )
