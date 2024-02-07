from urllib.parse import urljoin

from Scrapers.Scraper import Scraper


class TevapharmScraper(Scraper):
    name = "טבע"
    url = "https://careers.teva/search/?q=&q2=&alertId=&locationsearch=&geolocation=&searchby=location&d=10&lat=&lon=&title=&shifttype=&facility=&location=&department=Israel%09"

    def scrape_page(self, soup):
        positions = soup.findAll("tr", class_="data-row")
        for job in positions:
            title = job.findNext("span", class_="jobTitle").text.strip()
            link = job.findNext("span", class_="jobTitle").find("a")["href"]
            location = job.findNext("span", class_="jobLocation").text.strip()
            self.positions.append(
                self.Position(
                    title=title,
                    link=urljoin("https://careers.teva/search/", link),
                    location=location
                )
            )

    def scrape(self):
        soup = self.scraping_unit(self.url)
        self.scrape_page(soup)
        pages = soup.find("ul", class_="pagination").findAll("li")
        pages = pages[2:-1]
        for pg in pages:
            sub_url = pg.findNext('a')["href"]
            soup = self.scraping_unit(urljoin("https://careers.teva/search/", sub_url))
            self.scrape_page(soup)
