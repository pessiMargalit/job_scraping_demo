
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class WishingwellScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/embed/job_board?for=wishingwellvet&b=https%3A%2F%2Fwishingwell-vet.com%2Fcareers%2F"
    name = 'Wishingwell'

    def scrape(self):
        super().scrape()

