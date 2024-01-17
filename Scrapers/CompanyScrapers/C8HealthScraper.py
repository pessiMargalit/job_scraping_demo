from bs4 import BeautifulSoup

from Scrapers.Scraper import Scraper


class C8HealthScraper(Scraper):
    name = 'C8 Health'
    url = 'https://c8health.com/careers/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'col content-box-wrapper content-wrapper-background link-area-box link-type-text content-icon-wrapper-yes icon-hover-animation-fade'}):
            link = div_tag ['data-link']
            driver = self.selenium_url_maker(link)
            soup_job = BeautifulSoup(driver.page_source, 'html.parser')
            title = soup_job.find('h3', {'class': 'fusion-title-heading title-heading-left fusion-responsive-typography-calculated'})
            location = soup_job.find('h4', {'class': 'fusion-title-heading title-heading-left fusion-responsive-typography-calculated'})

            self.positions.append(self.Position(
                title=title.text,
                location=location.text if location else None,
                link=link
            ))


C8HealthScraper().check_self()