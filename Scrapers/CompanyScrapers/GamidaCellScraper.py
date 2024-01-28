
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class GamidaCellScraper(GreenhouseScraper):
    name = 'GamidaCell'
    url = GreenhouseScraper.url.format(name)
