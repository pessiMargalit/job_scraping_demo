from Scrapers.Scraper import *


class EisnerAmperScraper(Scraper):
    name = 'EisnerAmper'
    base_url = 'https://careers.eisneramper.com/'
    url = f'{base_url}en/career-opportunities/'
    location = 'Jerusalem'

    def calculate_num_of_career_pages(self):
        soup = self.scraping_unit(self.url)
        num_pages = soup.find_all('li', {'class': 'page-item'})
        num = num_pages[-2].text
        return int(num)

    def scrape(self):
        num_pages = self.calculate_num_of_career_pages() + 1
        for i in range(1, num_pages):
            soup = self.scraping_unit(f'{self.url}?page={i}#header')
            positions = soup.find_all(
                attrs={'class': "card card-job"})
            for pos in positions:
                title = pos.findNext('h2', {'class': "card-title"})
                link = pos.findNext('a', {"class": "stretched-link js-view-job"})
                metadata = pos.findAllNext('li', {"class": "list-inline-item"})
                content = metadata[0]
                location = metadata[1]
                self.positions.append(self.Position(
                    title=title.text.strip() if title else None,
                    link=f'{self.base_url}{link["href"]}' if link else self.url,
                    location=location.text.strip() if location else self.location,
                    content=content.text.strip() if content else None
                ))
