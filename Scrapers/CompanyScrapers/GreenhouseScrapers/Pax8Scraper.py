
from ScrapingTools.OutsourceTools.Greenhouse.BaseScraper import GreenhouseScraper


class Pax8(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/embed/job_board?for=pax8&b=https%3A%2F%2Fwww.pax8.com%2Fen-us%2Fpax8-careers%2F"
    name = 'pax8'

    def scrape(self):
        super().scrape()

