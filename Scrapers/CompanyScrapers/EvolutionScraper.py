
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class EvolutionScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/embed/job_board?for=peibio&b=https%3A%2F%2Fprotein-evolution.com%2Fcareers"
    name = 'EVolution'

    def scrape(self):
        super().scrape()

