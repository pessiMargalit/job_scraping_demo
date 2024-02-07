from Scrapers.Scraper import Scraper


class GlobaNetworksScraper(Scraper):
    name = "גלובל נטוורקס"
    location = "הר חוצבים, ירושלים"
    url = "https://glnet.co.il/%d7%93%d7%a8%d7%95%d7%a9%d7%99%d7%9d/"

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.findAll("div", class_=lambda class_: class_ and class_.startswith(
            "elementor-column elementor-col-50 elementor-top-column elementor-element"))
        for position in positions:
            title = position.findNext("span", class_="elementor-button-text").text.strip()
            self.positions.append(
                self.Position(
                    title=title,
                    link=self.url
                )
            )


GlobaNetworksScraper().check_self()
