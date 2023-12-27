from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class AxoniusScraper(GreenhouseScraper):
    url = "https://www.axonius.com/company/careers/open-jobs"
    name = 'Axonius'

    def scrape(self):
        self.find_greenhouse_url(self.url)
        self.url = self.url.replace("/js", "")
        super().scrape()


AxoniusScraper().check_self()
