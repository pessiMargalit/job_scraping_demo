from Scrapers.Scraper import Scraper


class MizrahiScraper(Scraper):
    name = "mizrahi"
    url = "https://www.mizrahi-tefahot.co.il/about-mizrahi-tefahot-he/career/open-jobs/"

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'job filterItem'}):
            title = div_tag.findNext('h3').text.strip()
            location = div_tag.findNext('div', {'class': 'location'}).text.strip()
            link = self.url
            self.positions.append(self.Position(
                title=title,
                location=location,
                link=link
            ))