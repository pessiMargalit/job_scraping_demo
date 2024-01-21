from Scrapers.Scraper import Scraper


class QuantlrScraper(Scraper):
    name = 'QuantLR'
    url = 'https://quantlr.com/careers/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'elementor-post__text'}):
            title = div_tag.findNext('h4', {'class': 'elementor-post__title'})
            link = title.findNext('a')['href']
            self.positions.append(self.Position(
                title=title.text.strip(),
                link=link
            ))


