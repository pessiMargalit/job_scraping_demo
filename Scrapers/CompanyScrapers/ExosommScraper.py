from Scrapers.Scraper import Scraper


class ExosommScraper(Scraper):
    name = 'Exosomm'
    url = 'https://www.exosomm.com/careers'

    def scrape(self):
        soup = self.scraping_unit(self.url)

        for div_tag in soup.findAll('div', {"data-mesh-id":"comp-l5fma59xinlineContent-gridContainer"}):
            title = div_tag.find('p', {'class': 'font_9 wixui-rich-text__text'})

            self.positions.append(self.Position(
                title=title.text,
                link=self.url
            ))


ExosommScraper().check_self()