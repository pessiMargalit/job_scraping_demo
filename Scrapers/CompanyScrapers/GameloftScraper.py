from Scrapers.Scraper import *


class GameloftScraper(Scraper):
    name = "Gameloft"
    url = 'https://careers.smartrecruiters.com/Gameloft'


    def scrape(self):
            soup = self.scraping_unit(self.url)
            careers = soup.find_all('li', class_='opening-job job column wide-7of16 medium-1of2')
            for job in careers:
                title = job.findNext('h4', class_='details-title job-title link--block-target').text.strip()
                link = job.findNext('a', class_='link--block details')['href']
                # location = areas[area]
                self.positions.append(self.Position(
                    title=title,
                    link=link,
                    # location=location
                ))


GameloftScraper().check_self()
