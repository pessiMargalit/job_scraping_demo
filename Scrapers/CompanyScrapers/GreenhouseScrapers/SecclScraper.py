
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class SecclScraper(GreenhouseScraper): 
    url = "https://boards.eu.greenhouse.io/embed/job_board?for=seccltechnology&b=https%3A%2F%2Fseccl.tech%2Fcareers%2Frole%2Fqa-engineer%2F"
    name = 'Seccl'

    def scrape(self):
        super().scrape()

