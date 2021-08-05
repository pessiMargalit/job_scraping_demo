from Scrapers.Scraper import *


class SimilarWebScraper(Scraper):
    name = 'SimilarWeb'
    url = 'https://boards.greenhouse.io/similarweb'
    location = 'Tel-Aviv, Israel'
    __base_url = 'https://www.similarweb.com'

    def __init__(self):
        super(SimilarWebScraper, self).__init__()

    def scrape(self):
        soup = self.scraping_unit(self.url)

        for pos in soup.findAll('div', attrs={'class': 'opening'}):
            a_tag = pos.findNext('a')
            self._company_positions.append(
                self.Position(
                    title=a_tag.text.strip(),
                    link=f"https://boards.greenhouse.io{a_tag['href']}",
                    location=pos.findNext('span', attrs={'class': 'location'}).text.strip(),
                    tags=pos.findPrevious('h2').text.strip(),
                    company_url=self.__base_url
                )
            )
