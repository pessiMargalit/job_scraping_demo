from Scrapers.Scraper import *


class C2AScraper(Scraper):
    name = 'C2A Security'
    url = 'https://c2a-sec.com/careers/'

    def scrape(self):
        soup = self.scraping_unit(self.url)

        # Find all divs with class containing "jet-listing-grid__item jet-listing-dynamic-post" ending with "5678"
        careers = soup.select('div[class^="jet-listing-grid__item jet-listing-dynamic-post"]')
        for job in careers:
            title = job.find_next('span')
            link = job.find_next('a', class_='elementor-button elementor-button-link elementor-size-sm')

            if title:
                self.positions.append(self.Position(
                    title=title.text.strip() if title else None,
                    link=link['href'] if link else None,
                ))
