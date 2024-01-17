import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from Scrapers.Scraper import Scraper


class GoogleScraper(Scraper):
    name = 'Google'
    url = 'https://www.google.com/about/careers/applications/jobs/results/'

    def calculate_max_iteration(self):
        soup = self.scraping_unit(self.url)
        div_element = soup.find('div', {'jsname': 'uEp2ad'})
        text_content = div_element.text.strip()
        # Use regular expressions to extract numeric values
        match = re.match(r'(\d+)[^\d]+(\d+)', text_content)
        jobs_per_page = int(match.group(2))
        total_jobs = int(text_content.split(' ')[-1])
        return (total_jobs // jobs_per_page) + 1

    def specific_page_url(self, index):
        string_index = f"?page={index}"
        return urljoin(self.url, string_index)

    def scrape(self):
        iteration = 0
        max_iteration = self.calculate_max_iteration()

        while iteration < max_iteration:
            iteration += 1
            driver = self.selenium_url_maker(self.specific_page_url(iteration))
            try:
                updated_page_source = driver.page_source

                # Parse the updated page source with BeautifulSoup
                soup = BeautifulSoup(updated_page_source, 'html.parser')

                # Loop through job elements and extract information
                for div_tag in soup.findAll('div', {'class': 'sMn82b'}):
                    title = div_tag.findNext('h3', {"class": "QJPWVe"}).text
                    link = div_tag.findNext('a')['href']
                    location = div_tag.findNext('span', {"class": "r0wTof"}).text

                    self.positions.append(self.Position(
                        title=title,
                        link=link,
                        location=location
                    ))
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                driver.quit()


GoogleScraper().check_self()

