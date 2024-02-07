from urllib.parse import urljoin
from Scrapers.Scraper import *


class AdenzaScraper(Scraper):
    url = 'https://adenza.pinpointhq.com/postings.json?_=1707217241591'
    name = 'Adenza'

    def __init__(self):
        super(AdenzaScraper, self).__init__()

    def scrape(self):
        response = requests.get(self.url,verify=False)
        response = response.json()
        for pos in response['data']:
            title = pos['title']
            link = pos['url']
            location = pos['location']['city']
            self.positions.append(self.Position(
                title=title.strip(),
                link=link,
                location=location
            ))

