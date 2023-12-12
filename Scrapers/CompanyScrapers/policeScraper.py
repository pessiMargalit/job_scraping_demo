from Scrapers.Scraper import *


class PoliceScraper(Scraper):
    name = 'Police'
    url = 'https://www.police.gov.il/join/CandidateForm/jobs'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div in soup.findAll('div', {"class": "jobBlock"}):
            title = div.findNext('h3')
            content = div.findNext('div', {'class': 'text'})
            # location = div.findNext('div', {'class': 'text'})
            self.positions.append(self.Position(
                title=title.text,
                link=div['href'],
                # location=location.text,
                content=content.text
            ))
    #   def scrape(self):
    #     # Use selenium to wait for the page to load
    #     driver = self.selenium_url_maker(self.url)
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, 'jobBlock'))
    #     )
    #     # Use BeautifulSoup to parse the driver.page_source
    #     soup = BeautifulSoup(driver.page_source, 'html.parser')
    #     soup = self.scraping_unit(driver.current_url)
    #     # Process the page with BeautifulSoup
    #     for div in soup.findAll('div', {"class": "jobBlock"}):
    #         title = div.findNext('h3')
    #         content = div.findNext('div', {'class': 'text'})
    #         # location = div.findNext('div', {'class': 'text'})
    #         self.positions.append(self.Position(
    #             title=title.text,
    #             link=self.url,
    #             # location=location.text,
    #             content=content.text
    #         ))
    #
    #     # Close the driver when done
    #     driver.quit()


PoliceScraper().check_self(content=True)
