
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class NomadHealthScraper(GreenhouseScraper):
    name = 'Nomad Health'
    url = GreenhouseScraper.url.format(name)

