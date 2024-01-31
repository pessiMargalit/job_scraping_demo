from Scrapers.Scraper import *


class ComeetScraper(Scraper):
    url = ''
    name = ''

    def scrape(self):
        response = requests.get(self.url)
        jobs_line = [line.decode() for line in response.content.splitlines() if
                     "COMPANY_POSITIONS_DATA" in line.decode() and '=' in line.decode()][0]
        json_line_str = jobs_line.split("=", 1)[1]
        jobs_array = json.loads(json_line_str[:-1])

        for job in jobs_array:
            location = job.get('location')
            if location:
                location = location.get('name')
            else:
                location = 'HQ'
            job_url = job.get('url_active_page')
            if job_url.count('/') == 3:
                job_url = job.get('position_url')
            if not job_url or job_url.count('/') == 3:
                job_url = job.get('url_comeet_hosted_page')
            self.positions.append(
                self.Position(
                    title=job.get('name'),
                    link=job_url,
                    location=location,
                )
            )
