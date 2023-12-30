
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class HandshakeScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/embed/job_board?for=joinhandshake"
    name = 'Handshake'

    def scrape(self):
        super().scrape()

