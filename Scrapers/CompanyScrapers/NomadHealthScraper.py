
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraperJson import GreenhouseScraperJson


class NomadHealthScraper(GreenhouseScraperJson):
    name = 'NomadHealth'
    url = GreenhouseScraperJson.url.format(name)

