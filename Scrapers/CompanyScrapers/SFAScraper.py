from Scrapers.Scraper import *


class SFAScraper(Scraper):
    name = 'SFA'
    url = 'https://www.sfa.law/%d7%a7%d7%a8%d7%99%d7%99%d7%a8%d7%94/'
    location = 'ירושלים'
    optional_locations = ['ירושלים', 'חיפה', 'תל אביב']

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all('div', {'class': 'position-single accordion-section'})
        for pos in positions:
            title = pos.findNext('div', {'class': 'position--title accordion-section-title'})
            pos_location = pos.findPrevious('h3')
            while pos_location.text.strip() not in self.optional_locations:
                pos_location = pos_location.findPrevious('h3')
            location = pos_location
            details = pos.findNext('div', class_=lambda x: x and 'position--details accordion-section-content' in x)
            self.positions.append(self.Position(
                title=title.text.strip() if title else None,
                location=location.text.strip() if location else self.location,
                content=details.text.strip() if details else None
            ))
