
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class ToriiScraper(GreenhouseScraper):
    official_url = "https://www.toriihq.com/careers"
    url = "https://boards.greenhouse.io/embed/job_board?for=toriihq&b=https%3A%2F%2Fwww.toriihq.com%2Fjobs"
    name = 'Torii'

    def scrape(self):
        super().scrape()


ToriiScraper().check_self()
