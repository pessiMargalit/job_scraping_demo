
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraperJson import GreenhouseScraperJson


class GamidaCellScraper(GreenhouseScraperJson):
    name = 'GamidaCell'
    url = GreenhouseScraperJson.url.format(name)
