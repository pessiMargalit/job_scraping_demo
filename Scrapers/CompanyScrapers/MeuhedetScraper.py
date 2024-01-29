from Scrapers.Scraper import *


class MeuhedetScraper(Scraper):
    name = 'מאוחדת'
    url = 'https://www.meuhedet.co.il/search?mod=400'
    location = 'Jerusalem'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source)
        # soup = self.scraping_unit(self.url)
        positions = soup.find('div', {"class": "container"})
        print(positions)
        # for pos in positions:
        #     position = pos.findAllNext('font', {"color": "darkorange"})
        #     if len(position) >= 2:
        #         title = position[0]
        #         content = position[1]
        #         link = pos.findNext('a')['href']
        #         self.positions.append(self.Position(
        #             title=title.text if title else title,
        #             link=f'{self.base_url}/{link}',
        #             content=content.text if content else None
        #         ))


MeuhedetScraper().scrape()
