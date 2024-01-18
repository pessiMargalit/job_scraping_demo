from Scrapers.Scraper import *

# has only email for send
class NeteeraScraper(Scraper):
    name = 'Neteera'
    url = 'https://www.neteera.com/careers'
    # why is it unknown location
    location = 'UNKNOWN'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for div_tag in soup.findAll('div', {'class':"LWbAav Kv1aVt"}):
            title=div_tag.findNext('span',{'class':'wixui-rich-text__text'}).text
            self.positions.append(self.Position(
                title=title,
                link=self.url,
            ))


