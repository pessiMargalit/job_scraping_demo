from Scrapers.Scraper import Scraper


class ReubinofLawyerScraper(Scraper):
    name = "גבריאל ראובינוף - משרד עו''ד"
    url = "https://reubinof.co.il/%d7%a2%d7%91%d7%95%d7%93%d7%94-%d7%91%d7%a8%d7%90%d7%95%d7%91%d7%99%d7%a0%d7%95%d7%a3/"

    def scrape(self):
        soup = self.scraping_unit(self.url)
        positions = soup.find("div", class_="elementor-element elementor-element-1ae74ae elementor-widget elementor-widget-text-editor")
# "elementor-element elementor-element-1ae74ae elementor-widget elementor-widget-text-editor"
# "elementor-element elementor-element-baa9ee5 elementor-widget elementor-widget-text-editor"

        for pos in positions:
            title = pos.text.strip()
            print(title)
