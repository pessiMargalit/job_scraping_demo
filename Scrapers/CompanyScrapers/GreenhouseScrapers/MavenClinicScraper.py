
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class MavenClinicScraper(GreenhouseScraper):
    official_url = "https://www.mavenclinic.com/careers"
    url = "https://boards.greenhouse.io/mavenclinic"
    name = 'Maven Clinic'

    def scrape(self):
        super().scrape()


MavenClinicScraper().check_self()
