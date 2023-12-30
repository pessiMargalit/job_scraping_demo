
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseScraper import GreenhouseScraper


class AppsflyerScraper(GreenhouseScraper): 
    url = "https://boards.greenhouse.io/appsflyer/jobs/6916762002?utm_source=Qumra+Capital+job+board&utm_medium=getro.com&gh_src=Qumra+Capital+job+board"
    name = 'AppsFlyer'

    def scrape(self):
        super().scrape()

