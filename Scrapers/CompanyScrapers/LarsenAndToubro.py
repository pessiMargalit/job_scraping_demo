from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 60


class LarsenAndToubroScraper(Scraper):
    name = 'Larsen & Toubro'
    url = 'https://larsentoubrocareers.peoplestrong.com/job/joblist'
    location = 'Jerusalem'

    def calculate_page_jobs_amount(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'card-block-inner'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup)
        num_of_pages = soup.findNext('ul', {'class': "pagination pull-right hoverActive"})
        # print(num_of_pages)
        # return int(num_of_pages[2:])

    def scrape(self):
        driver = self.selenium_url_maker(self.url)
        WebDriverWait(driver, TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'card-block-inner'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        button = soup.findAll('span', {'class': 'material-icons keyboard_arrow_right md24'})
        # for li in soup.findAll('span', {'class': 'material-icons keyboard_arrow_right md24'}):
        print(button)


            # for div in soup.findAll('div', {'class': 'card-block-inner'}):
            #     title = div.findNext('a', {'class': 'link'})
            #     location = div.findNext('ul', {'class': 'list-reset clearfix listing-inline'}).findNext('li').findNext('li')
            #     position_url = title['href']
            #     base_url = self.url[:45]
            #     link =f'{base_url}{position_url}'
            #     self.positions.append(self.Position(
            #         title=title.text if title else None,
            #         link=link if link else self.url,
            #         location=location.text.strip() if location else None,
            #     ))


# LarsenAndToubroScraper().check_self()
LarsenAndToubroScraper().calculate_page_jobs_amount()