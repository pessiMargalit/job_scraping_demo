from Scrapers.Scraper import *


class CieloInertialScraper(Scraper):
    name = 'Cielo Inertial Solutions'
    location = 'Israel'
    url = 'https://www.cielo-inertial.com/careers/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find_all('div', {"class": "rowT1"})
        for job in careers:
            title = job.findNext('div', class_='text')
            link = job.findNext('a', class_='btn_job btn_blue btn')
            # content = job.findNext('a', class_='btn_job btn_blue btn')
            if title:
                self.positions.append(self.Position(
                    title=title.text if title else None,
                    link=link['href'] if link else None,
                    # content=content.text if content else None
                ))

