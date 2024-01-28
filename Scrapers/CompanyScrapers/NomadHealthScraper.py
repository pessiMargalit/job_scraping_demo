
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class NomadHealthScraper(GreenhouseScraper):
    name = 'NomadHealth'
    url = GreenhouseScraper.url.format(name)

