
from ScrapingTools.OutsourceTools.Comeet.ComeetScraper import ComeetScraper


class CognyteScraper(ComeetScraper):
    url = "https://www.cognyte.com/careers/il/"
    name = "Cognyte"

CognyteScraper().check_self()