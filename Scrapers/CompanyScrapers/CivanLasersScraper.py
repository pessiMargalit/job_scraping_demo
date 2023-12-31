from Scrapers.Scraper import *


class CivanLasersScraper(Scraper):
    name = 'Calypsa'
    location = 'Jerusalem'
    url = 'https://www.staging.civanlasers.com/careers'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        jobs = soup.find('section', {'id': "comp-kv42h6z3"})
        careers = jobs.findAll('div', {'data-testid': "richTextElement"})
        for job in careers:
            title = job.find_next('span', {'class': "wixui-rich-text__text"})
            link = job.find_next('a')
            if title:
                self.positions.append(self.Position(
                    title=title.text.strip() if title else None,
                    link=link['href'] if link else None,
                ))
