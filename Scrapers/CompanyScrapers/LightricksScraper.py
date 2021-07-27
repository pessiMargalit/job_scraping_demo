
from Scrapers.Scraper import *


class LightricksScraper(Scraper):
    url = 'https://www.lightricks.com/careers'
    name = 'Lightricks'
    location = 'Jerusalem'

    def __init__(self):
        super(LightricksScraper, self).__init__()
        self.__base_url = "https://www.lightricks.com"

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('a', attrs={'class': 'w-inline-block'}):
            if not a_tag.parent.attrs.get('class') or 'w-dyn-item' not in a_tag.parent.attrs.get('class'):
                continue
            title = a_tag.text.strip()
            location = a_tag.findPrevious('h1', id="open-positions", attrs={'class': 'h3'}).text.split('-')[-1].strip()
            t_time = a_tag.findNext('h4', attrs={'class': 'part-time'}).text.strip()
            self._company_positions.append(
                self.Position(
                    title=title,
                    link=self.__base_url + a_tag['href'],
                    location=location,
                    time_type=t_time,
                    tags=a_tag.findPrevious('h1', attrs={'class': 'h3 light'}).text.strip(),
                    company_url=self.__base_url
                )
            )
