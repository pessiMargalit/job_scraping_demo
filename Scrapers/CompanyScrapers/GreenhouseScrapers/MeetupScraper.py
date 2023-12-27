
from Scrapers.CompanyScrapers.GreenhouseScrapers.GreenhouseScraper import GreenhouseScraper


class MeetupScraper(GreenhouseScraper):
    official_url = "https://www.meetup.com/careers/"
    url = "nan"
    name = 'Meetup'

    def scrape(self):
        super().scrape()


MeetupScraper().check_self()
