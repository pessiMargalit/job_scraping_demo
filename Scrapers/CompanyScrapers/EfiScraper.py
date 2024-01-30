from concurrent.futures import ThreadPoolExecutor

from Scrapers.Scraper import *


class EfiScraper(Scraper):
    name = 'Efi'
    # url = 'https://phe.tbe.taleo.net/phe03/ats/careers/v2/searchResults?next&rowFrom={}' \
    #       '&act=search&sortColumn=null&sortOrder=null&currentTime=1706608095791'
    url = 'https://www.efi.com/about-efi/careers/job-search/'
    location = 'Jerusalem'

    # def scrape_page(self):
    #     driver = self.selenium_url_maker(self.url)
    #     button_locator = (By.CLASS_NAME, "btn.btn-primary.oracletaleocwsv2-btn-fa.fa-search")
    #     print(button_locator)
    #     button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(button_locator))
    #     button.click()
    #     soup = self.scraping_unit(driver.page_source)
    #     positions = soup.find_all(attrs={'class': "oracletaleocwsv2-accordion-head-info"})
    #     for pos in positions:
    #         print(pos)
        #     title = pos.findNext('h4', {'class': "oracletaleocwsv2-head-title"})
        #     link = pos.findNext('a', {"class": "viewJobLink"})
        #     location = pos.findNext('div')
            # self.positions.append(self.Position(
            #     title=title.text.strip() if title else None,
            #     link=link["href"] if link else self.url,
            #     location=location.text.strip() if location else self.location,
            # ))

    def scrape_page(self, page):
        soup = self.scraping_unit(self.url.format(page))
        positions = soup.find_all(attrs={'class': "oracletaleocwsv2-accordion-head-info"})
        for pos in positions:
            title = pos.findNext('h4', {'class': "oracletaleocwsv2-head-title"})
            link = pos.findNext('a', {"class": "viewJobLink"})
            location = pos.findNext('div')
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
                link=link["href"] if link else self.url,
                location=location.text.strip() if location else self.location,
            ))

    def scrape(self):
        num_pages = 50
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.scrape_page, i) for i in range(10, num_pages + 1, 10)]
            # Wait for all futures to complete
            for future in futures:
                future.result()


EfiScraper().check_self()
