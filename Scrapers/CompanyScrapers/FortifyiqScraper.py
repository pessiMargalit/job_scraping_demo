
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class FortifyiqScraper(GreenhouseScraper): 
    name = 'FortifyIQ'
    url = GreenhouseScraper.url.format(name)


