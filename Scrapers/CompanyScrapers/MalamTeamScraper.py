from Scrapers.Scraper import *


class MalamTeamScraper(Scraper):
    name = "MalamTeam"
    url = 'https://www.malamteam.com/%d7%aa%d7%95%d7%a6%d7%90%d7%95%d7%aa-%d7%97%d7%99%d7%a4%d7%95%d7%a9-%d7%9e%d7%a9%d7%a8%d7%95%d7%aa/'

        def scrape(self):
            # url: a=60 means location=Jerusalem
            # for all the jobs: a= empty
            soup = self.scraping_unit(f"{self.url}?pr=&a={60}&t=", )
            careers = soup.find_all('div', class_='search-result-row item-row')
            for job in careers:
                title = job.findNext('div', class_='job-name').text.strip()
                link = job.findNext('div', class_='item-col col-btn').find('a')['href']
            self.positions.append(self.Position(
            title=title,
            link=link
                        ))