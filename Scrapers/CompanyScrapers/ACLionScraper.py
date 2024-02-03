from Scrapers.Scraper import *


class ACLionScraper(Scraper):
    name = 'AC Lion'
    url = 'https://aclion.com/job-search/'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all(attrs={'class': 'job'})
        for pos in positions:
            title = pos.findNext('h4')
            link = pos.findNext('a')
            location = pos.findNext('span', {'class': 'location'})
            content = pos.findNext('span', {'class': 'salary'})
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
                link=link['href'] if link else self.url,
                location=location.text.strip() if location else self.location,
                content=content.text.strip() if content else None
            ))
