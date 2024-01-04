from Scrapers.Scraper import *


class RegencorScraper(Scraper):
    name = "Regencor"
    url = 'https://www.regencor.com/careers'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find_all('div', class_='accordion-header js-accordion-header')

        for job in careers:
            link = self.url
            title = job.findNext('h3', class_='career__headline').text.strip()
            description = job.findNext('p', class_="paragraph-normal").text.strip()
            self.positions.append(self.Position(
                title=title,
                link=link,
                content=description,
            ))

