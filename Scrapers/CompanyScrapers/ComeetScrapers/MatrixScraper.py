
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class MatrixScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/matrix-ifs/19.00F"
    name = "Matrix"

    def scrape(self):
        super().scrape()

    