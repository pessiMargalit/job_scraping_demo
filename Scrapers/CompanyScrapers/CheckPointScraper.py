from Scrapers.Scraper import *


class CheckPointScraper(Scraper):
    url = 'https://careers.checkpoint.com/?q=&module=cpcareers&a=search&fa%5B%5D=country_ss%3AIsrael&sort='
    name = 'CheckPoint'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        position_results = soup.find('div', id='positionResults')
        for job in position_results.findAll('div', class_='position'):
            title = job.findNext('a').text.strip()
            title = title.strip('\n')
            link = job.findNext('a')['href']
            info = job.findNext('div', class_='posInfo')
            location = info.findNext('p').text.strip()
            # the location is in the first p tag, the tag doesn't have any specific identifier.
            self.positions.append(
                self.Position(
                    title=title,
                    link=link,
                    location=location
                )
            )

