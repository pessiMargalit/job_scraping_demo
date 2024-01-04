from Scrapers.Scraper import Scraper


class HydroxScraper(Scraper):
    name = 'Hydrox'
    url = 'https://hydrox.earth/hydro-x-careers/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'elementor-post__text'}):
            title = div_tag.findNext('h3', {'class': 'elementor-post__title'})
            link = div_tag.findNext('a')['href']
            self.positions.append(self.Position(
                title=title.text,
                link=link
            ))


HydroxScraper().check_self()
