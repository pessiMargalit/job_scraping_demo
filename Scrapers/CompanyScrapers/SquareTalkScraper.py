from Scrapers.Scraper import *


class SquareTalkScraper(Scraper):
    name = 'SquareTalk'
    url = 'https://squaretalk.com/career/#rec_job_listing_div'
    # TODO: ask if it is needed to because there is only jobs at Bulgaria
    location = 'Bulgaria'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = self.scraping_unit(self.url)
        data=driver.find_elements(By.CLASS_NAME,'rec-job-info')
        for ul in data:
            title=ul.find_element(By.CLASS_NAME,'rec-job-title')
            link=title.find_element(By.TAG_NAME,'a').get_attribute('href')
            self.positions.append(self.Position(
                title=title.text,
                link=link,
            ))




