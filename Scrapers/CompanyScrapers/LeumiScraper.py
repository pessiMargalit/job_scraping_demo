import re

from Scrapers.Scraper import Scraper


class LeumiScraper(Scraper):
    name = "leumi"
    url = "https://www.leumi.co.il/leumi_main/searchjobs"

    def scrape(self):
        soup = self.scraping_unit(self.url)
        table_tag = soup.find('div', {'class': 'table-body'})
        for div_tag in table_tag.findAll('div', {'class': lambda x: x and re.match('table-row row-', x)}):
            title = div_tag.findNext('div', {'class': 'role-title'}).findNext('button').text.strip()
            # this code is because of problems with white spaces
            location = div_tag.findNext('div', {'class': 'area'}).text[5:].strip()
            # if there are multi places
            if len(location) > 20:
                location = location.replace('\n', '')
                location = re.sub(r'\s+', ' ', location)
            # the job description and sending CV in on the same page
            link = self.url
            self.positions.append(self.Position(
                title=title,
                location=location,
                link=link
            ))