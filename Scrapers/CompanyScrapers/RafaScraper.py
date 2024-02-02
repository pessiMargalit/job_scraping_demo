from Scrapers.Scraper import *


class RafaScraper(Scraper):
    name = 'Rafa'
    url = 'https://www.rafa.co.il/careers'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        pattern = re.compile(r'<a\s+href="(https://www\.rafa\.co\.il/page/\d+)">(.*?)<\/a>', re.UNICODE)

        for div_position in soup.find_all('p'):
            div_position_str = str(div_position)
            matches = pattern.findall(div_position_str)

            for link, title in matches:
                self.positions.append(self.Position(
                    title=title,
                    link=link,
                ))


