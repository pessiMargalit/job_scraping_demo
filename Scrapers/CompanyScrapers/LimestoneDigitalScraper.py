from Scrapers.Scraper import *


class LimestoneDigitalScraper(Scraper):
    name = "LimestoneDigital"
    url = 'https://limestonedigital.com/careers/'


    def scrape(self):
            soup = self.scraping_unit(self.url)
            careers = soup.find_all('div', class_='vacancy-card')

            for job in careers:
                title = job.findNext('a', class_='vacancy-card-title').text.strip()
                link = job.findNext('a', class_='vacancy-card-title')['href']
                # location = find it in the link...
                self.positions.append(self.Position(
                    title=title,
                    link=link,
                    location='remote'
                ))

