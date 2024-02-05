
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraperJson import GreenhouseScraperJson


class FortifyiqScraper(GreenhouseScraperJson):
    name = 'FortifyIQ'
    url = GreenhouseScraperJson.url.format(name)


