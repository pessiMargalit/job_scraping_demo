from Scrapers.Scraper import *


class RevelatorScraper(Scraper):
    name = 'Revelator'
    url = 'https://revelator.recruitee.com/'

    def scrape(self):
        soup = self.scraping_unit(self.url)
        careers = soup.find_all('div', {'class': 'sc-6exb5d-2 ftcjTl'})
        for job in careers:
            job_title_and_location = job.findNext('a')
            # Find the main span element with class "sc-6exb5d-5"
            main_span = soup.find('span', class_='sc-6exb5d-5')

            # Extract individual location components
            location_remote = main_span.select_one('.sc-1s8re0d-0.jpykjQ').text.strip()
            location_city = main_span.select_one('.custom-css-style-job-location-city').text.strip()
            location_region = main_span.select_one('.custom-css-style-job-location-region').text.strip()
            location_country = main_span.select_one('.custom-css-style-job-location-country').text.strip()

            # Concatenate the location components
            location = f'{location_remote} {location_city},{location_region},{location_country}'
            if job_title_and_location:
                self.positions.append(self.Position(
                    title=job_title_and_location.text if job_title_and_location else None,
                    link=f"{self.url}{job_title_and_location['href']}" if job_title_and_location else None,
                    location=location
                ))

