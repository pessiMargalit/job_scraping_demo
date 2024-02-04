from urllib.parse import urljoin
from Scrapers.Scraper import *


class AlynHospitalScraper(Scraper):
    name = 'Alyn Hospital'
    url = 'https://www.alyn.org.il/%D7%93%D7%A8%D7%95%D7%A9%D7%99%D7%9D'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        h2_tags = soup.findAll(lambda tag: tag.name == 'h2' and'דרוש' in tag.text)
        for tag in h2_tags:
            title = tag.text
            id_job = tag.get('id')
            link = urljoin(self.url, f"#{id_job}")
            self.positions.append(self.Position(
                title=title.strip(),
                link=link,
                location=self.location
            ))
