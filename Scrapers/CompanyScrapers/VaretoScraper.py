
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraperJson import GreenhouseScraperJson


class VaretoScraper(GreenhouseScraperJson):
    name = 'vareto'
    url = GreenhouseScraperJson.url.format(name)
