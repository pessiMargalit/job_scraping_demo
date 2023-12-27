
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class NomadHealthScraper(GreenhouseScraper):
    official_url = "https://nomadhealth.com/careers"
    url = "https://boards.greenhouse.io/nomadhealth"
    name = 'Nomad Health'

    def scrape(self):
        super().scrape()


NomadHealthScraper().check_self()
