
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class VaretoScraper(GreenhouseScraper):
    name = 'vareto'
    url = GreenhouseScraper.url.format(name)
