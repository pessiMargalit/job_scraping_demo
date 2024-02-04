from Scrapers.Scraper import *


class SitehoodScraper(Scraper):
    name = 'Sitehood'
    url = 'https://www.sitehood.co.il/%D7%93%D7%A8%D7%95%D7%A9%D7%99%D7%9D/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        # Use BeautifulSoup to find all div elements with the class "fusion-column-wrapper" on the page
        # [1:-1] is used to exclude the first element (header) and the last element (footer) from the list
        jobs = soup.find_all('div', {'class': "fusion-column-wrapper"})[1:-1]
        for job in jobs:
            title = job.find_next('h2')
            content = job.find_next('div')
            match = re.search(r"מיקום המשרה: (.+?)\.", content.text)
            location = match.group(1) if match else None
            self.positions.append(self.Position(
                title=title.text if title else None,
                location=location,
                content=content.text if content else None
            ))
