
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class OpenAIScraper(GreenhouseScraper):
    official_url = "https://openai.com/careers"
    url = "https://boards.greenhouse.io/openai"
    name = 'OpenAI'

    def scrape(self):
        super().scrape()


OpenAIScraper().check_self()
