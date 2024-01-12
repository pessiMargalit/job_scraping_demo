import time


def run_scraper_test(scraper):
    scraper.scrape()
    return len(scraper.get_positions()) > 0


def run_scraper_and_get_positions(scraper):
    scraper.scrape()
    return scraper.get_positions()

def validate_url(url):
    return url.startswith('http')


def check_scraper_performance(start_time, end_time, max_duration=90):
    return end_time - start_time < max_duration
