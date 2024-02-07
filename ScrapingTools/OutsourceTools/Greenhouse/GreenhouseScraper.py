from Scrapers.Scraper import *


class GreenhouseScraper(Scraper):
    name = ''
    url = 'https://boards.greenhouse.io/'
    api_url = 'https://api.greenhouse.io/v1/boards/{}/embed/jobs'
    json_url = api_url.format(name)
    name = 'Greenhouse'

    def scrape_json(self):
        response = requests.get(self.json_url)
        response_json = response.json()
        for job in response_json.get('jobs'):
            self.positions.append(
                self.Position(
                    title=job['title'].strip(),
                    link=job['absolute_url'].strip(),
                    location=job['location']['name'].strip()
                )
            )

    def scrape_normal(self):
        soup = self.scraping_unit(self.url)
        for position_div in soup.findAll('div', {'class': 'opening'}):
            title = position_div.findNext('a')
            location = position_div.findNext('span', {'class': 'location'})
            link = title['href'] if title else None
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
                link=f'{self.url}{link}',
                location=location.text.strip() if location else None
            ))

    def scrape(self):
        try:
            self.scrape_json()
        except Exception as e:
            self.scrape_normal()
