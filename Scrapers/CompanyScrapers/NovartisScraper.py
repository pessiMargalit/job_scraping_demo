import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from Scrapers.Scraper import Scraper


class NovartisScraper(Scraper):
    name = 'Novartis'
    url = 'https://www.novartis.com/careers/career-search?search_api_fulltext=&country%5B%5D=LOC_IL&field_alternative_country%5B%5D=LOC_IL&early_talent=All&field_job_posted_date=All'
    max = 2

    def calculate_max_iteration(self):
        soup = self.scraping_unit(self.url)
        last_page = soup.find('li', {'class': 'page-item pager__item--last'})
        if last_page:
            last_page = int(last_page.getText())
            return last_page - 1
        return 1

    def scrape(self):
        iteration = 0
        max_iteration = self.calculate_max_iteration()

        while iteration < max_iteration:
            iteration += 1
            driver = self.selenium_url_maker(self.url)
            try:
                updated_page_source = driver.page_source

                # Parse the updated page source with BeautifulSoup
                soup = BeautifulSoup(updated_page_source, 'html.parser')

                # Loop through job elements and extract information
                for tr_tag in soup.findAll('tr', {'tabindex': '0'}):
                    title = tr_tag.findNext('a', {"hreflang": "en"}).text

                    link = tr_tag.findNext('a')['href']

                    location = tr_tag.findNext('td', {"headers": "view-field-job-work-location-table-column"}).text

                    self.positions.append(self.Position(
                        title=title.strip(),
                        link=urljoin(self.url, link),
                        location=location.strip()
                    ))
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                driver.quit()


