
    from ScrapingTools.OutsourceTools.Comeet.BaseScraper import ComeetScraper
    

    class Abrascraper(ComeetScraper):
        url = "https://www.comeet.com/jobs/abra/12.003"
        name = "Abra"

        def scrape(self):
            super().scrape()

    