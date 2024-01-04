from Scrapers.Scraper import Scraper


class GenetikaPlusScraper(Scraper):
    name = 'Genetika+'
    url = 'https://www.genetikaplus.com/careers#Open-Positions'

    def scrape(self):
        location = None
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'w-dyn-item'}):
            title = div_tag.findNext('h3', {'class': 'heading-style-h6'})
            all_description_items = div_tag.findNext('div', {'class': 'positions_descrription-wrapper'})
            description_items = all_description_items.findAll('div', {'class': 'positions-descrription_item'})
            if len(description_items) > 1:
                location = description_items[1]
            link_tag = div_tag.findNext('a')
            link = link_tag['href']
            if link != '#':
                self.positions.append(self.Position(
                    title=title.text,
                    location=location.text if location else None,
                    link=link
                ))


GenetikaPlusScraper().check_self()
