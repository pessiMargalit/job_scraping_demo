
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class LivepersonScraper(GreenhouseScraper):
    official_url = "https://www.liveperson.com/company/careers/"
    url = "https://boards.greenhouse.io/embed/job_board?for=liveperson"
    name = 'Liveperson'

    def scrape(self):
        super().scrape()


LivepersonScraper().check_self()
