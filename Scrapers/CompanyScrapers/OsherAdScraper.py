from Scrapers.Scraper import Scraper


class OsherAdScraper(Scraper):
    url = "https://osherad.co.il/drushim/"
    name = "אושר עד"

    def scrape(self):
        soup = self.scraping_unit(self.url)
        lst = soup.find("div", class_="jet-listing-grid__items grid-col-desk-1 grid-col-tablet-1 grid-col-mobile-1 jet-listing-grid--3229")
        jobs = lst.findAll("div", class_="jet-listing-grid__item")
        for job in jobs:
            title = job.findNext("h2", class_="elementor-heading-title elementor-size-default")
            title = title.text.strip().removeprefix("דרוש: ")
            location = job.findNext("span",class_="elementor-icon-list-text")
            location = location.text.strip().removeprefix("מיקום: ")
            self.positions.append(
                self.Position(
                    title=title,
                    location=location,
                    link=self.url
                )
            )

