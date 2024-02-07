from Scrapers.Scraper import *


class Maayan2000Scraper(Scraper):
    name = 'מעיין 2000'
    url = 'https://opensheet.elk.sh/1yS2scu28A4lazXabAmscTo23bu4NXc5UAx56SQcl_eg/db!A1:D1000'
    career_url = 'https://api.whatsapp.com/send?phone=972502329612&text=%D7%A9%D7%9C%D7%95%D7%9D%20%D7%A8%D7%91,%20%D7%9E%D7%AA%D7%A2%D7%A0%D7%99%D7%99%D7%A0/%D7%AA%20%D7%91%D7%9E%D7%A9%D7%A8%D7%94%20%D7%91%D7%A2%D7%99%D7%A8:%20%D7%91%D7%A0%D7%99%20%D7%91%D7%A8%D7%A7,%20%D7%91%D7%AA%D7%A4%D7%A7%D7%99%D7%93:%20%D7%A1%D7%93%D7%A8%D7%9F/%D7%99%D7%AA',

    def scrape(self):
        response = requests.get(self.url, verify=False)
        response = response.json()
        for pos in response:
            if pos['active'] == 'כן':
                title = pos['name']
                location = pos['city']
                self.positions.append(self.Position(
                    title=title.strip(),
                    link=self.career_url[0],
                    location=location
                ))

