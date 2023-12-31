from Scrapers.Scraper import *


class OwnBackupScraper(Scraper):
    name = 'OwnBackup'
    url = 'https://www.owndata.com/careers#section-jobs'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        class_pattern = re.compile(r'job job-(\d+) jobs-item')
        careers = soup.find_all('div', class_=class_pattern)
        for job in careers:
            title = job.find_next('div', {'class': 'title jobs-title is--margin-25'})
            link = job.find_next('a', class_='sub-title')

            if title:
                self.positions.append(self.Position(
                    title=title.text.strip() if title else None,
                    link=link['href'] if link else None,
                ))


OwnBackupScraper().check_self()
