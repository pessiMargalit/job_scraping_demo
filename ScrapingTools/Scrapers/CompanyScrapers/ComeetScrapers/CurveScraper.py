
    from ScrapingTools.OutsourceTools.Comeet.BaseScraper import ComeetScraper
    

    class Curvescraper(ComeetScraper):
        url = "https://www.comeet.com/jobs/curve/E4.001"
        name = "Curve"

        def scrape(self):
            super().scrape()

    