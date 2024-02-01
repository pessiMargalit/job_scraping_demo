import re

from Scrapers.Scraper import Scraper


class OmnixMedicalScraper(Scraper):
    name = 'Omnix Medical'
    url = "https://omnixmedical.com/careers/"

    def scrape(self):
        soup = self.scraping_unit(self.url)

        h2_tags = soup.find_all('h2', class_="elementor-heading-title elementor-size-default")
        for h2_tag in h2_tags:
            if re.search(r'<font\s+color="#A5D14A"[^>]*>', str(h2_tag)):
                title = h2_tag.text.strip()
                self.positions.append(self.Position(
                    title=title.replace("\n", " ").replace("  ", " "),
                    link=self.url
                ))
