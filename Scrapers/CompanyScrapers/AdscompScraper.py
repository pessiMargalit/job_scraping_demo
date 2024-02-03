from Scrapers.Scraper import Scraper


class AdscompScraper(Scraper):
    url = "https://adscomp.co.il/he/wanted_h.php"
    name = "א.ד.ס. סודרי מחשבים"

    def scrape(self):
        soup = self.scraping_unit(self.url)
        table = soup.find("table")
        lst = table.findAll("tr")
        jobs = lst[1]
        titles = jobs.findAllNext("u")
        content = jobs.findAllNext("font", {'color': '#993300'})
        for i, title in enumerate(titles):
            self.positions.append(
                self.Position(
                    title=title.text.strip(),
                    content=content[i].text.strip(),
                    link=self.url
                )
            )

