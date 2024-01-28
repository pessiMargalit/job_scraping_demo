
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class CodefreshScraper(GreenhouseScraper): 
    name = 'Codefresh'
    url = GreenhouseScraper.url.format(name)

