from Scrapers.Scraper import *
import concurrent.futures


class LeumitScraper(Scraper):
    name = 'לאומית'
    base_url = 'https://www.leumit.co.il'
    url = f'{base_url}/heb/Useful/jobs/jobopennings/'
    location = 'ירושלים'

    def scrape_url(self, url):
        soup = self.scraping_unit(url)
        positions = []
        for div in soup.findAll('div', {'class': 'ArticleShort span4'}):
            title = div.findNext('h2').text.strip() if div.findNext('h2') else None
            location = div.findNext('pre').text.strip() if div.findNext('pre') else None
            link = div.findNext('a')['href'] if div.findNext('a') else None
            link = f"{self.base_url}{link}"
            positions.append(self.Position(
                title=title,
                location=location,
                link=link
            ))
        return positions

    def get_all_categories_urls(self):
        soup = self.scraping_unit(self.url)
        for div in soup.findAll('div', {'class': 'ArticleShort span12'}):
            careers_url = div.findNext('a')['href']
            yield careers_url

    def scrape(self):
        self.positions = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            url_jobs = [executor.submit(self.scrape_url, url) for url in self.get_all_categories_urls()]
            for job in concurrent.futures.as_completed(url_jobs):
                self.positions.extend(job.result())


LeumitScraper().check_self()
