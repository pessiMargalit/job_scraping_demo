from Scrapers.Scraper import *


class UdiMariliScraper(Scraper):
    name = 'Udi Marili'
    url = 'https://www.udimarili.co.il/Jobs'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.findAll('div', {'id': '1332374166'})
        all_details = positions[0].findAllNext('div', {'class': 'dmRespColsWrapper'})
        for detail in all_details[:2]:
            pos_detail = detail.findAllNext('span', {'class': 'lh-1'})
            title = pos_detail[1]
            location = pos_detail[3]
            self.positions.append(self.Position(
                title=title.text[11:].strip() if title else None,
                location=location.text.strip() if location else self.location
            ))
