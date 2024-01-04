from Scrapers.Scraper import *
from urllib.parse import quote

TIMEOUT_IN_SECONDS = 30


class EggXYtScraper(Scraper):
    url = 'https://www.eggxyt.com/'
    name = 'EggXYt'

    def collect_urls(self):
        driver = self.selenium_url_maker(self.url)
        jobs_links = WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, 'a')))
        # soup.find_all('a',
        #                        href=lambda href: href and href.startswith("/search") and href.endswith("/jobs"))
        print(jobs_links)
        # urls = [a_tag['href'] for a_tag in jobs_links]
        # print(urls)
        return jobs_links

    def scrape(self):
        positions_urls = EggXYtScraper().collect_urls()
        # for position_url in positions_urls:
        #     positions_urls = quote(position_url, safe=':/')
        #     soup = self.scraping_unit(positions_urls)
        #     for div in soup.findAll('div', {'class': 'job-item'}):
        #         title = div.findNext('h2', {'class': 'job-title'})
        #         location = div.findNext('b', {'class': 'job-areas'})
        #         link = quote(title.findNext('a')['href'], safe=':/')
        #         if self.location in location.text:
        #             self.positions.append(self.Position(
        #                 title=title.text if title else None,
        #                 link=link if link else self.url,
        #                 location=location.text if location else None,
        #             ))


EggXYtScraper().scrape()
