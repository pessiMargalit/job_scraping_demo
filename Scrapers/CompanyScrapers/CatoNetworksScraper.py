
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class CatoNetworksScraper(GreenhouseScraper):
    url = "https://boards.eu.greenhouse.io/embed/job_board?for=catonetworks&b=https%3A%2F%2Fwww.catonetworks.com%2Fcareers%2Fcareers-post%2F4190151101%2F"
    name = 'Cato Networks'

    def scrape(self):
        super().scrape()

