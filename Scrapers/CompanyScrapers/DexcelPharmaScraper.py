from Scrapers.Scraper import *


class DexcelPharmaScraper(Scraper):
    name = 'Dexcel Pharma'
    url = 'https://www.dexcel.com/careers'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find_all('div', {"role": "listitem"})
        for job in careers:
            title = job.findNext('div', class_='text-block-43')
            content = job.findNext('div', class_='open-dropdown')
            if title:
                self.positions.append(self.Position(
                    title=title.text,
                    link=self.url,
                    content=content.text if content else None
                ))