
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class PlacerAiScraper(GreenhouseScraper):
    official_url = "https://www.placer.ai/company/we-are-hiring"
    url = "https://boards.greenhouse.io/embed/job_board?for=placerlabs"
    name = 'Placer.ai'

    def scrape(self):
        # self.find_greenhouse_url(self.url)
        super().scrape()


PlacerAiScraper().check_self()
