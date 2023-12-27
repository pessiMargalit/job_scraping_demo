from Scrapers.Scraper import *

class GreenhouseScraper(Scraper):
    base_url = 'https://boards.greenhouse.io/'
    url = 'https://boards.greenhouse.io/'
    name = 'Greenhouse'

    def find_greenhouse_url(self, official_site_url):
        pass
        # try:
        #     # Send a GET request to the URL
        #     headers = {
        #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        #                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        #     response = requests.get(official_site_url, headers=headers)
        #     response.raise_for_status()  # Raise an exception for bad responses
        #     soup = BeautifulSoup(response.text, 'html.parser')
        #     greenhouse_link = soup.find('a', href=re.compile(r'.*greenhouse.io.*'))
        #     self.url = greenhouse_link['href'] if greenhouse_link else self.url
        #     if greenhouse_link is None:
        #         greenhouse_link = soup.find('script', src=re.compile(r'.*greenhouse.io.*'))
        #         self.url = greenhouse_link.get('src') if greenhouse_link else self.url
        # except requests.exceptions.RequestException as e:
        #     print("Error:", e)
        # except Exception as e:
        #     print("HTTP Error 418: Blocked by NetFree: ", e)

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for position_div in soup.findAll('div', {'class': 'opening'}):
            title = position_div.findNext('a')
            location = position_div.findNext('span', {'class': 'location'})
            link = title['href'] if title else None
            self.positions.append(self.Position(
                title=title.text if title else None,
                link=f'{self.base_url}{link}',
                location=location.text if location else None
            ))