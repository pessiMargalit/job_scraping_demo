
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class EdgybeesScraper(ComeetScraper):
    url = "https://www.comeet.com/jobs/edgybees/95.000"
    name = "Edgybees"

EdgybeesScraper().check_self()