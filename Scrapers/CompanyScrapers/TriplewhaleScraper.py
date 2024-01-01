from Scrapers.Scraper import *

TIMEOUT_IN_SECONDS = 10


class TriplewhaleScraper(Scraper):
    name = 'Triplewhale'
    url = 'https://www.triplewhale.com/careers'

    def scrape(self):
        driver = self.selenium_url_maker(self.url)

        try:
            # Wait for the lever-jobs-container to be present on the page
            jobs_container = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'lever-jobs-container'))
            )

            # Now that the jobs container is present, find all the li elements
            for li in jobs_container.find_elements(By.CLASS_NAME, 'lever-job'):
                career = li.find_element(By.CLASS_NAME, 'lever-job-title')
                location = li.find_element(By.TAG_NAME, 'span')
                self.positions.append(self.Position(
                    title=career.text.strip() if career else None,
                    link=career.get_attribute('href') if career else None,
                    location=location.text.strip() if location else None
                ))
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            driver.quit()  # Make sure to close the browser even if an exception occurs


TriplewhaleScraper().check_self()
