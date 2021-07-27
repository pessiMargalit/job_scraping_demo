from Scrapers.Scraper import *


class FacebookScraper(Scraper):
    name = 'Facebook'
    url = 'https://www.facebook.com/careers/jobs/?offices%5B0%5D=Tel+Aviv%2C+Israel&is_leadership=0&results_per_page=100&is_in_page=1'
    location = "Tel Aviv"

    def __init__(self):
        super(FacebookScraper, self).__init__()

    def scrape(self):
        soup = self.scraping_unit(self.url)

        num_of_positions = -1
        try:
            num_of_positions_div = (soup.find("div", text=re.compile('Viewing \d+ - \d+ of \d+')))
            num_of_positions = int(num_of_positions_div.text.split(' ')[-1])
        except:
            print("IDK how many jobs facebook have so i'll just guess one page is enough")
        bowls = [soup]
        if num_of_positions != -1 and num_of_positions > 100:

            for i in range(101, num_of_positions, 100):
                page_number = (int(i/100) + 1)
                next_page_url = f"{self.url[:-1]}{page_number}"
                bowls.append(self.scraping_unit(next_page_url))
        for soup in bowls:
            a_tags = soup.findAll('a', href=re.compile('/careers/v2/jobs/'))
            for pos in a_tags:
                children = pos.findChildren('div', text=re.compile(" "), recursive=True)
                title = children[0].text
                tags = children[-1].text
                self._company_positions.append(
                    self.Position(
                        title=title,
                        link=f"https://www.facebook.com{pos['href']}",
                        location="Tel Aviv",
                        tags=tags
                    )
                )
