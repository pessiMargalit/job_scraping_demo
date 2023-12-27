
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class LightricksScraper(GreenhouseScraper):
    official_url = "https://careers.lightricks.com/"
    url = "https://boards.greenhouse.io/embed/job_board?for=lightricks"
    name = 'Lightricks'

    def scrape(self):
        super().scrape()


LightricksScraper().check_self()
