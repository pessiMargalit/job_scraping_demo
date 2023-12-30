
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class NomadhealthScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/nomadhealth"
    name = 'Nomad Health'

    def scrape(self):
        super().scrape()

