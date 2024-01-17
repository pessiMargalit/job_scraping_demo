from Scrapers.Scraper import *


class OwnBackupScraper(Scraper):
    name = 'OwnBackup'
    url = 'https://www.owndata.com/careers#section-jobs'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find_all('div', class_='div-block-37')
        for job in careers:
            title = job.find_next('div', {'class': 'title jobs-title is--margin-25'})
            link = job.find_next('a', class_='sub-title')
            location = job.find_next('div', class_='location')
            if title:
                self.positions.append(self.Position(
                    title=title.text if title else None,
                    link=link['href'] if link else None,
                    location=location.text if location else None
                ))
