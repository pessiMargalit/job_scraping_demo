from Scrapers.Scraper import *


class AirDoctorScraper(Scraper):
    name = 'Air Doctor'
    url = 'https://www.air-dr.com/careers'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find_all('div', {'class': 'eael-call-to-action cta-basic bg-lite cta-preset-1'})
        for job in careers:
            title = job.find_next('h4')
            link = job.find_next('a', class_='sub-title')

            if title:
                self.positions.append(self.Position(
                    title=title.text.strip() if title else None,
                    link=link['href'] if link else None,
                ))

