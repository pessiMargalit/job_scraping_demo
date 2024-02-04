from Scrapers.Scraper import Scraper


class EvisionSystemsScraper(Scraper):
    name = 'Evision Systems'
    url = 'https://evision-systems.com/company/career/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        jobs = soup.find('div', {'class': 'et_pb_section et_pb_section_1 et_section_regular'})
        for div_tag in jobs.findAll('div', {'class': 'et_pb_text_inner'}):
            title = div_tag.findNext('h3')
            self.positions.append(self.Position(
                title=title.text,
                link=self.url
            ))


