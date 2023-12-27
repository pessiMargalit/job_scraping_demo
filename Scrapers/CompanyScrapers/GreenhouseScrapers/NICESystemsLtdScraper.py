
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class NICESystemsLtdScraper(GreenhouseScraper):
    official_url = "https://www.nice.com/careers/apply"
    url = "https://boards.eu.greenhouse.io/nice"
    name = 'NICE Systems Ltd'

    def scrape(self):
        super().scrape()


NICESystemsLtdScraper().check_self()
