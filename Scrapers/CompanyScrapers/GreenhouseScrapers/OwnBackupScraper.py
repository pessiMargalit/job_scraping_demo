
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class OwnBackupScraper(GreenhouseScraper):
    official_url = "https://www.owndata.com/careers"
    url = "nan"
    name = 'OwnBackup'

    def scrape(self):
        super().scrape()


OwnBackupScraper().check_self()
