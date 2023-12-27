
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class ValeraHealthScraper(GreenhouseScraper):
    official_url = "https://www.valerahealth.com/careers/"
    url = "https://boards.greenhouse.io/embed/job_board?for=valerahealth&b=https%3A%2F%2Fwww.valerahealth.com%2Fcareers%2F"
    name = 'Valera Health'

    def scrape(self):
        super().scrape()


ValeraHealthScraper().check_self()
