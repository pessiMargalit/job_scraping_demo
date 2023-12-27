from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class GongIoScraper(GreenhouseScraper):
    official_url = "https://www.gong.io/careers/"
    url = "https://boards.greenhouse.io/gongio"
    name = 'Gong.io'

    def scrape(self):
        super().scrape()


GongIoScraper().check_self()
