from Scrapers.Scraper import *


class AthenagoScraper(Scraper):
    url = 'https://jobs.athenago.com/'
    name = 'Athenago'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find('div', class_='job-postings-list w-dyn-items')
        for job in careers:
            title = job.findNext('div', class_='r-text r-h2 custom-postings').text
            location = job.findNext('div', class_='r-text custom-jobpostings').text
            link = job.findNext('a', {'id': 'w-node-fa070411-7419-e9e7-198e-34a562c555c0-49bb5997'})['href']
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))
