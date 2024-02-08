from bs4 import BeautifulSoup

from Scrapers.Scraper import Scraper


class MercantileSscraper(Scraper):
    name = "mercantile"
    url = "https://www.mercantile.co.il/private/about-mercantile/career/"

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        div_tag = soup.find('div', {'class': 'faq-items-wrap accordeon add-bottom-space'})
        for h4_tag in div_tag.findAllNext('h4', {'class': 'question accordeon-title'}):
            title = h4_tag.text.strip()
            job_content = h4_tag.findNextSibling('div', {'class': 'answer accordeon-content rte-content'})
            p_tag_rtl = job_content.find('strong').findParent()
            location = p_tag_rtl.text.replace('מיקום', '').replace(':', '').strip()
            if location == "בהתאם לתקנים הקיימים בסניפים":
                location = ""
                for li in p_tag_rtl.findNextSibling('ul'):
                    location += li.text.strip()
            # the job content is on the same page
            link = self.url
            self.positions.append(self.Position(
                title=title,
                location=location,
                link=link
            ))