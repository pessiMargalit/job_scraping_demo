from Scrapers.Scraper import *


class DDSScraper(Scraper):
    name = 'DDS'
    url = 'https://www.vscyberhosting3.com/dds/Careers.aspx?type=CAREERSMAIN'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        table = soup.find('table', {'id': 'CRCareers1_tblTableDetail2'})
        for tr_tag in table.findAll('tr')[1:]:
            a_tag = tr_tag.findNext('a', {'class': 'JobLink'})
            title = a_tag.text
            link = a_tag['href']
            location = tr_tag.findNext('td').findNext('td').text
            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))