
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class AxoniusScraper(GreenhouseScraper):
    official_url = "https://www.axonius.com/company/careers/open-jobs"
    url = "https://boards.greenhouse.io/embed/job_board?for=Axonius"
    name = 'Axonius'

    def scrape(self):
        super().scrape()


AxoniusScraper().check_self()
