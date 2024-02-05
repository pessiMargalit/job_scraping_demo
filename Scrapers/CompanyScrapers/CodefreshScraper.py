
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraperJson import GreenhouseScraperJson


class CodefreshScraper(GreenhouseScraperJson):
    name = 'Codefresh'
    url = GreenhouseScraperJson.url.format(name)

