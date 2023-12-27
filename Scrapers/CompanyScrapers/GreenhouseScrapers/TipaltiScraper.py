
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class TipaltiScraper(GreenhouseScraper):
    official_url = "https://tipalti.com/careers/"
    url = "https://boards.greenhouse.io/embed/job_board?for=tipaltisolutions&b=https%3A%2F%2Ftipalti.com%2Fcareers%2F"
    name = 'Tipalti'

    def scrape(self):
        super().scrape()


TipaltiScraper().check_self()
