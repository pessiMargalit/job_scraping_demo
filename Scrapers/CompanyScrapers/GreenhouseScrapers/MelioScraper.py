
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class MelioScraper(GreenhouseScraper):
    official_url = "https://careers.meliopayments.com/"
    url = "https://boards.greenhouse.io/melio/"
    name = 'Melio'

    def scrape(self):
        super().scrape()


MelioScraper().check_self()
