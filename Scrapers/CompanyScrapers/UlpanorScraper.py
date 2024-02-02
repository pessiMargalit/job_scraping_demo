from urllib.parse import urljoin

from Scrapers.Scraper import Scraper


class UlpanorScraper(Scraper):
    url = "https://www.ulpanor.com/career/"
    name = "אולפן אור"

    def scrape(self):
        soup = self.scraping_unit(self.url)
        lst = soup.find("ul", class_="vc_tta-tabs-list")
        jobs = lst.findAll("li")
        for job in jobs:
            title = job.text.strip()
            link = job.findNext("a")["href"]
            self.positions.append(
                self.Position(
                    title=title,
                    link=urljoin(self.url, link)
                )
            )

