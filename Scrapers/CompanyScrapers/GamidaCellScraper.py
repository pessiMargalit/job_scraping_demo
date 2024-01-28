
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class GamidaCellScraper(GreenhouseScraper):
    name = 'Gamida Cell'
    url = GreenhouseScraper.url.format(name)
