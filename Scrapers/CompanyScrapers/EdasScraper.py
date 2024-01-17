from Scrapers.Scraper import *


# has duplicates and None values because the div and a tag have no unique class name
class EdasScraper(Scraper):
    name = 'edas'
    url = 'https://edas.tech/careers/'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class': 'elementor-widget-wrap elementor-element-populated'}):
            all_title = div_tag.findNext('h4', {'class': 'elementor-heading-title elementor-size-default'})
            title = all_title.text if all_title else None
            print(title)
            # location = div_tag.findNext('span', {'class': 'NormalTextRun SCXW178148966 BCX9'})
            # link = div_tag.findNext('a', {'class': 'elementor-button elementor-button-link elementor-size-sm'})['href']
            # self.positions.append(self.Position(
            #     title=title.text if title else None,
            #     link=link if link and link != '#opening' else None,
            #     # location=location.text if location else None
            # ))


