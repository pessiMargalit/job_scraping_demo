import time


def run_scraper_test(scraper):
    scraper.scrape()
    return len(scraper.get_positions()) > 0, time.time()


def check_scraper_performance(start_time, end_time, max_duration=90):
    return end_time - start_time < max_duration
