from Scrapers.Scraper import Scraper


class NvidiaScraper(Scraper):
    name = 'Invidia'
    url = 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        print(soup)
        for li_tag in soup.findAll('ul'):
            title = li_tag.findNext('h3')
            location = li_tag.findNext('div', {"class": "css-248241"})
            self.positions.append(self.Position(
                title=title.text,
                link=title.find_next('href'),
                location=location.text
            ))


NvidiaScraper().check_self()
