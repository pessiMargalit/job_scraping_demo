from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Scrapers.Scraper import Scraper

TIMEOUT_IN_SECONDS = 60


class AlphaTauScraper(Scraper):
    name = 'Alpha Tau'
    #  original URL: 'https://www.alphatau.com/careers' but the jobs are at a different URL
    url = 'https://www.powr.io/plugins/job-board/wix_view?lang=en&dateNumberFormat=en-us&isPrimaryLanguage=true&pageId=hc85f&compId=TPASection_k9wgzbp5&viewerCompId=TPASection_k9wgzbp5&siteRevision=3845&viewMode=site&deviceType=desktop&locale=en&regionalLanguage=en&width=980&height=938&instance=eV8hqapVR8UfqvpZpu8skZshCn42DAE1UwQ2M57FMmA.eyJpbnN0YW5jZUlkIjoiNTAzMGZmMjItY2M5OC00YzAzLWIwZTItYTgzYzQxNjQ4ZWMzIiwiYXBwRGVmSWQiOiIxMzBmZTM1Ni02NWEyLWY2YTAtZDgyZS03NWQ2YWExZGRmNmIiLCJzaWduRGF0ZSI6IjIwMjMtMTItMzFUMDg6MDM6MTQuNDgwWiIsInZlbmRvclByb2R1Y3RJZCI6InBybyIsImRlbW9Nb2RlIjpmYWxzZSwiYWlkIjoiZWI0NmIyNmEtZmRjMC00NGMyLTgzYWYtN2FhZDJmZDkxYzUzIiwic2l0ZU93bmVySWQiOiI3NDkyNWRmYS1kYWJhLTQ0ZjItYTIzNi1mYmY3MmM3NzU2YTEifQ&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22host%22%3A%22VIEWER%22%2C%22bsi%22%3A%2231aec756-b6d1-4d13-9755-ec145bc2a4e4%7C1%22%2C%22BSI%22%3A%2231aec756-b6d1-4d13-9755-ec145bc2a4e4%7C1%22%7D&currentRoute=.%2Fcareers&target=_top&section-url=https%3A%2F%2Fwww.alphatau.com%2Fcareers%2F&vsi=435f461a-bf1c-4f3f-9bae-83341f54ffd0&mirror=surgeFactoryInstantResume'
    location = 'Jerusalem'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jobBoard"))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        jobs = soup.find('div', {'class': 'jobBoard row softLightShadow'})
        for div_tag in jobs.findAll('div', {'class': 'row jobListing'}):
            title = div_tag.findNext('h4', {'class': 'jobTitle'})
            p_tag = div_tag.findNext('p', {'class': 'details inline'})
            location = p_tag.text.split("•")[0]
            self.positions.append(self.Position(
                title=title.text,
                location=location if location else None,
                link=self.url
            ))
        driver.quit()


