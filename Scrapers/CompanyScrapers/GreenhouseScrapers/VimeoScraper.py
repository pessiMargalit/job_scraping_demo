
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class VimeoScraper(GreenhouseScraper):
    official_url = "https://vimeo.com/careers"
    url = "https://boards.greenhouse.io/vimeo"
    name = 'Vimeo'

    def scrape(self):
        super().scrape()


VimeoScraper().check_self()
