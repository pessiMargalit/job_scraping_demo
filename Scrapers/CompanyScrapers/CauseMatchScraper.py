from Scrapers.Scraper import *


class CauseMatchScraper(Scraper):
    name = 'Cause match'
    url = 'https://www.causematch.com/careers/'
    location = 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        i = 1
        for div in soup.findAll('div', {'class': 'elementor-widget-wrap elementor-element-populated'}):
            # title = div.findNext('h3', {'class': 'elementor-heading-title elementor-size-default'})
            # location = div.findNext('div', {'class': 'elementor-element elementor-element-84ebce0 elementor-widget elementor-widget-text-editor'})
            # link = div.findNext('a', {'class': 'elementor-button elementor-button-link elementor-size-xs'})
            # i += 1
            h3_tag = soup.find('h3', class_='elementor-heading-title elementor-size-default')
            p_tags = soup.find_all('p')
            a_tag = soup.find('a', class_='elementor-button elementor-button-link elementor-size-xs')

            print('title:',h3_tag.text)
            print("location",p_tags)
            print('link',a_tag['href'])
            # self.positions.append(self.Position(
            #     title=title.text if title else None,
            #     link=link.get('href') if link else self.url,
            #     location=location.text.strip() if location else None,
            # ))


CauseMatchScraper().check_self()


