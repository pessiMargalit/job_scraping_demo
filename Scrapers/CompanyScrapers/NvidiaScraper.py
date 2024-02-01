from ScrapingTools.OutsourceTools.MyWorkDay.MyWorkDayScraper import MyWorkDayScraper


class NvidiaScraper(MyWorkDayScraper):
    url = "https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite/jobs"
    name = "nvidia"