from Scrapers.Scraper import *


class InzivScraper(Scraper):
    name = 'Inziv'
    location = 'Jerusalem'
    url = 'https://inziv.com/careers/'

    def scraping_unit(self, url, headers=None):
        if headers:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url)

        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')

    def scrape(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        soup = self.scraping_unit(self.url, headers=headers)
        careers = soup.find('ul', {'class': 'comeet-positions-list'})
        for job in careers.find_all('li'):
            title = job.findNext('div', class_='comeet-position-name')
            content = job.findNext('div', class_='comeet-position-meta')
            link = job.findNext('a', class_='comeet-position')
            if title:
                self.positions.append(self.Position(
                    title=title.text,
                    link=f"https:{link['href']}" if link else None,
                    content=content.text if content else None
                ))


