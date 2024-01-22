from urllib.parse import urljoin

from Scrapers.Scraper import Scraper


class UBConnectScraper(Scraper):
    name = 'UBConnect'
    url = 'https://career.ubconnect.no/jobs'
    location = 'Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('li', {'class': "w-full"}):

            title = a_tag.findNext('span', {"class": "text-block-base-link sm:min-w-[25%] sm:truncate company-link-style"})
            title= title.get_text() if title else None
            location = a_tag.findNext('div', {'class': 'mt-1 text-md'})
            location=location.get_text() if location else None
            link=a_tag.findNext('a')['href']
            if title:
                self.positions.append(self.Position(
                    title=title,
                    link=urljoin(self.url, link),
                    location=location
                ))
UBConnectScraper().check_self()