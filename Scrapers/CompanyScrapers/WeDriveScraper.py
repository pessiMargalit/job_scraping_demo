from bs4 import BeautifulSoup

from Scrapers.Scraper import Scraper


class WeDriveScraper(Scraper):
    name = 'We Drive'
    url = 'https://wedriveauto.com/career-openings/'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        jobs = soup.find('div', {'class': 'gmail_default'})
        for li_tag in jobs.findAll('li'):
            location = None
            link = None
            title = li_tag
            link_tag = li_tag.find('a')
            if link_tag:
                link = link_tag['href']
                soupJob = self.scraping_unit(link)
                location = soupJob.find('h6', {'class': 'subtitle'})
            self.positions.append(self.Position(
                title=title.text,
                location=location.text if location else None,
                link=link if link else self.url
            ))
        driver.quit()


