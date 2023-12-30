
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class LightricksScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/lightricks/jobs/7011401002?utm_source=Qumra+Capital+job+board&utm_medium=getro.com&gh_src=Qumra+Capital+job+board"
    name = 'Lightricks'

    def scrape(self):
        super().scrape()

