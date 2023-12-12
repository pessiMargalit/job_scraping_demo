from Scrapers.Scraper import Scraper


class MobileyeScraper(Scraper):
    name = 'Mobileye'
    url = 'https://careers.mobileye.com/jobs'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        for a_tag in soup.findAll('a', {'class': 'card'}):
            print("a_tag", a_tag)
            h3_tag = a_tag.findNext('h3')
            location = a_tag.findNext('div', {'class': 'location'})
            self.positions.append(self.Position(
                title=h3_tag.text,
                link=a_tag['href'],
                location=location.text
            ))
MobileyeScraper().check_self()

class InvidiaScraper(Scraper):
    name = 'Invidia'
    url = 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite'
    location = 'west Jerusalem'  # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        print(soup.findAll())
        for li_tag in soup.findAll('li'):
            print("li_tag",li_tag)
            # h3_tag = li_tag.findNext('h3')
            # location = li_tag.findNext('div')
            # self.positions.append(self.Position(
            #     title=h3_tag.text,
            #     link=li_tag['href'],
            #     location=location.text
            # ))
InvidiaScraper().check_self()
