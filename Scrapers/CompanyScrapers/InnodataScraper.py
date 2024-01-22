from urllib.parse import urljoin

from Scrapers.Scraper import *
from bs4 import BeautifulSoup
# from msedge.selenium_tools import Edge, EdgeOptions


# the href is to js function

class InnodataScraper(Scraper):
    name = 'innodata'
    url = 'https://innodata.com/career/'

    # def get_edge_driver(url, debug=False, ssl_problems=False):
    #     edge_options = EdgeOptions()
    #     edge_options.use_chromium = True  # To use Edge Chromium
    #     edge_options.add_argument("--no-sandbox")
    #     edge_options.add_argument('--disable-dev-shm-usage')
    #     if not debug:
    #         edge_options.add_argument("--headless")
    #     if ssl_problems:
    #         edge_options.add_argument("--allow-running-insecure-content")
    #         edge_options.add_argument("--allow-insecure-localhost")
    #         edge_options.add_argument("--ignore-urlfetcher-cert-requests")
    #     driver = Edge(options=edge_options)
    #     driver.get(url)
    #     return driver

    def scrape(self):
        # driver = self.get_edge_driver(self.url)
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for ul_tag in soup.findAll('ul', {'class': 'elementor-icon-list-items elementor-inline-items'}):
            title, location = ul_tag.findNext('span', {'class': 'elementor-icon-list-text'}).text.strip().split('-')
            # can not get specifically to the modal although i took the modal id but it brings to the specific place
            # of the job on the web page
            link = self.url
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location.strip()
            ))
