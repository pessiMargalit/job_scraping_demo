from Scrapers.Scraper import *


class GreenhouseScraper(Scraper):
    base_url = 'https://boards.greenhouse.io/'
    url = 'https://boards.greenhouse.io/'
    name = 'Greenhouse'

    def scrape(self):
        # soup = self.scraping_unit(self.url)
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
        # for position_div in soup.findAll('div', {'class': 'opening'}):
        #     title = position_div.findNext('a')
        #     location = position_div.findNext('span', {'class': 'location'})
        #     link = title['href'] if title else None
        #     self.positions.append(self.Position(
        #         title=title.text.strip() if title else None,
        #         link=f'{self.base_url}{link}',
        #         location=location.text.strip() if location else None
        #     ))
