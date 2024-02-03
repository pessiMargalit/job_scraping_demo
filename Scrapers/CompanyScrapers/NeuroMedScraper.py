from bs4 import NavigableString

from Scrapers.Scraper import Scraper


class NeuroMedScraper(Scraper):
    url = 'https://neuromedinc.com/careers/'
    name = 'NeuroMed'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for p_tag in soup.find_all('p'):
            first_b = p_tag.find('b')
            if first_b and "Job Openings" in first_b.get_text(strip=True):
                siblings = list(first_b.next_siblings)
                title = siblings[1][len("Position: "):]
                location = siblings[3][len("Location: "):]
                description = siblings[5][len("Description: "):]
                self.positions.append(self.Position(
                    title=title,
                    location=location,
                    content=description
                ))

