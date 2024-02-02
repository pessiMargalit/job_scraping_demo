from Scrapers.Scraper import *


class LeverScraper(Scraper):
    name = "Lever"
    url = 'https://jobs.lever.co/factored'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find_all('div', class_='posting')
        for job in careers:
            link = job.findNext('a', class_="posting-title")['href']
            title = job.findNext('h5').text.strip()
            location = job.findNext('span',
                                    class_="display-inline-block small-category-label workplaceTypes").text.strip()
            location += job.findNext('span',
                                     class_="sort-by-location posting-category small-category-label location").text.strip()

            self.positions.append(self.Position(
                title=title,
                link=link,
                location=location
            ))
