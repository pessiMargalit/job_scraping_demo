from Scrapers.Scraper import *


class ChatterBoxScraper(Scraper):
    name = 'ChatterBox'
    url = 'https://careers.chatterbox.io/jobs'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find_all('a',
                                class_='flex flex-col py-6 text-center sm:px-6 hover:bg-gradient-block-base-bg focus-visible-company focus-visible:rounded')
        for job in careers:
            title = job.find_next('span',
                                  {'class': 'text-block-base-link sm:min-w-[25%] sm:truncate company-link-style'})
            link = job.find_next('a',
                                 class_='flex flex-col py-6 text-center sm:px-6 hover:bg-gradient-block-base-bg focus-visible-company focus-visible:rounded')
            locations = job.find_next('div', class_='mt-1 text-md').find_all('span')
            lst_location = [location.text.strip() for location in locations]
            location = ' '.join(lst_location)
            if title:
                self.positions.append(self.Position(
                    title=title.text if title else None,
                    link=link['href'] if link else None,
                    location=location if location else None
                ))
