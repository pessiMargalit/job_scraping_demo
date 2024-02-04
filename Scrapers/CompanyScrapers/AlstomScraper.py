from Scrapers.Scraper import *


class AlstomScraper(Scraper):
    name = 'Alstom'
    base_url = 'https://jobsearch.alstom.com'
    url = f'{base_url}/search/?createNewAlert=false&q=&locationsearch=Israel' \
          '&optionsFacetsDD_country=&optionsFacetsDD_department=&optionsFacetsDD_shifttype='
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find_all('div', {'class': 'jobdetail-phone visible-phone'})
        for pos in positions:
            detail = pos.findNext('a', {'class': 'jobTitle-link'})
            location = pos.findNext('span', {'class': 'jobLocation'})
            self.positions.append(self.Position(
                title=detail.text.strip() if detail else None,
                link=f"{self.base_url}{detail['href']}" if detail else self.url,
                location=location.text.strip() if location else self.location
            ))
