
    from ScrapingTools.OutsourceTools.Comeet.BaseScraper import ComeetScraper
    

    class Sundayskyscraper(ComeetScraper):
        url = "https://www.comeet.com/jobs/sundaysky/71.000"
        name = "SundaySky"

        def scrape(self):
            super().scrape()

    