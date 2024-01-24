
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class OpenaiScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/openai"
    name = 'OpenAI'

    def scrape(self):
        super().scrape()

