from ScrapingTools.OutsourceTools.MyWorkDay.MyWorkDayScraper import MyWorkDayScraper


class WattsScraper(MyWorkDayScraper):
    url = "https://wattswater.wd5.myworkdayjobs.com/wday/cxs/wattswater/External/jobs"
    name = "Watts water"