from Scrapers.Scraper import *
from urllib.parse import urljoin


class NanoDiamondScraper(Scraper):
    name = 'NanoDiamond'
    url = 'https://nanodiamond.co.il/career/'
    location = 'UNKNOWN'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'elementor-accordion-item'}):
            # the spliting is because of unuseful data which was filtered
            title = div_tag.findNext('a', {'class': 'elementor-accordion-title'}).text.split('.')[1:][0].strip()
            link_in_page = div_tag.find_next({'div': 'elementor-tab-content elementor-clearfix elementor-active'})['id']
            link = urljoin(self.url, '#' + link_in_page)
            self.positions.append(self.Position(
                title=title,
                link=link,
            ))
