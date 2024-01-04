from Scrapers.Scraper import *


class PrivatiseScraper(Scraper):
    name = "Privatise"
    url = 'https://www.privatise.com/careers/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find_all('div', class_="wpb_wrapper")

        for job in careers:
            title = job.findNext('span', style='font-family: Quicksand, sans-serif;')
            if title is not None:
                title = title.text.strip()
                link = self.url
                self.positions.append(self.Position(
                    title=title,
                    link=link,
                ))

