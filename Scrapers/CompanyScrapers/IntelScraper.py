from urllib.parse import urljoin

from Scrapers.Scraper import *


class IntelScraper(Scraper):
    name = 'Intel'
    base_url = 'https://jobs.intel.com'
    url = 'https://jobs.intel.com/en/search-jobs'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def calculate_page_jobs_amount(self):
        soup = self.scraping_unit(self.url)
        num_of_pages = soup.find('span', {'class': "pagination-total-pages"}).text
        return int(num_of_pages[2:])

    def specific_page_url(self, index):
        string_index = f"?results&p={index}"
        print(urljoin(self.url, string_index))
        return urljoin(self.url, string_index)

    def scrape(self):
        iteration = 0
        max_iteration = self.calculate_page_jobs_amount()
        while iteration < max_iteration:
            iteration += 1
            soup = self.scraping_unit(self.specific_page_url(iteration))
            try:
                for section in soup.findAll('div', {'class': 'search-title-location'}):
                    title = section.findNext('h2')
                    link = section.findNext('a', {'class': 'test-apply'})
                    location = section.findNext('span', {'class': 'job-location'})
                    self.positions.append(self.Position(
                        title=title.text if title else None,
                        link=urljoin(self.base_url, link['href']) if link else None,
                        location=location.text if location else None
                    ))
            except Exception as e:
                print(f"An error occurred: {e}")


IntelScraper().check_self()
