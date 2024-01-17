from urllib.parse import urljoin

from Scrapers.Scraper import *


# the href is to js function

class InnodataScraper(Scraper):
    name = 'innodata'
    url = 'https://innodata.com/career/'
    location = 'San Mateo, 101 S Ellsworth Ave, United States'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        driver = self.get_edge_driver(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for ul_tag in soup.findAll('ul', {'class': 'elementor-icon-list-items elementor-inline-items'}):
            title, location = ul_tag.findNext('span', {'class': 'elementor-icon-list-text'}).text.split('-')
            # can not get specifically to the modal although i took the modal id but it brings to the specific place
            # of the job on the web page
            modal_url = "#" + ul_tag.findNext('div', {'id': 'modal-af056e6'})['id']
            link = urljoin(self.url, modal_url)
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))

