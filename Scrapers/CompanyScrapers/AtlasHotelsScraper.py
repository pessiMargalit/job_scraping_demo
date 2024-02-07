from Scrapers.Scraper import *


class AtlasHotelsScraper(Scraper):
    url = 'https://www.atlas.co.il/careers/'
    name = 'Atlas'
    location = 'כל הארץ'

    def __init__(self):
        super(AtlasHotelsScraper, self).__init__()

    def scrape(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(self.url, headers=headers, verify=False)
        soup = BeautifulSoup(result.content, 'html.parser')
        for div in soup.find_all('div', {"class": 'job-card'}):
            title = div.findNext('h3', {'class': 'job-title'})
            link = div.findNext('a', {'class': 'btn btn-secondary job-link'})['href']
            self.positions.append(self.Position(
                title=title.text.strip(),
                link=link
            ))

