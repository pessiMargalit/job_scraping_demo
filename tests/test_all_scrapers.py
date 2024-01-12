import pytest
import time
from Scrapers.ScrapersFactory import ScrapersFactory
from test_utils import run_scraper_test, check_scraper_performance


@pytest.fixture(scope="session")
def factory():
    return ScrapersFactory()


def test_all_scrapers(factory):
    scraper_names = factory.get_scrapers_names()
    for name in scraper_names:
        scraper = factory.get_scraper_by_name(name)[0]
        assert scraper, f"Scraper {name} does not exist."

        start_time = time.time()
        has_positions, end_time = run_scraper_test(scraper)
        assert has_positions, f"Scraper {name} did not add any jobs."
        assert check_scraper_performance(start_time, end_time), f"Scraper {name} took longer than 1 minute."
