from urllib.parse import urljoin

from Scrapers.Scraper import *
from urllib.request import urlopen, Request


class RnetScraper(Scraper):
    name = 'Rnet'
    url = 'https://www.rnet-tech.com/index.php/careers'

    def scrape(self):
        # soup = self.scraping_unit(self.url)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }

        # Create a Request object with the specified headers
        request = Request(self.url, headers=headers)

        try:
            # Open the URL using the updated Request object
            with urlopen(request) as response:
                soup = BeautifulSoup(response, HTML_PARSER)
                for h1_tag in soup.findAll('h1', attrs={'itemprop': 'name'}):
                    data=h1_tag.findNext('a')
                    title=data.text
                    link = urljoin(self.url, data['href'])
                    self.positions.append(self.Position(
                        title=title.strip(),
                        link=link,
                    ))

        except Exception as e:
            print(f"An error occurred: {e}")