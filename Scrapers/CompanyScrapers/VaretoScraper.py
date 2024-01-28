
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class VaretoScraper(GreenhouseScraper): 
    url = GreenhouseScraper.url.format('vareto')
    name = 'Vareto'
