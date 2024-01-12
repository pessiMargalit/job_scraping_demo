import time

import pytest
from Scrapers.ScrapersFactory import ScrapersFactory
from test_utils import run_scraper_test, check_scraper_performance, run_scraper_and_get_positions, validate_url


@pytest.fixture(scope="session")
def factory():
    return ScrapersFactory()


def test_specific_company(factory, company_names):
    assert company_names, "No company names were given"


def test_scraper_existence(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_filename(name)
        assert scraper, f"Scraper {name} does not exist."


def test_scraper_name(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_filename(name)
        assert not scraper[0].name, f"Scraper {name} does not have a name."


def test_scraper_url(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_filename(name)
        assert not scraper[0].url, f"Scraper {name} does not have a default url."


def test_scarper_adds_jobs(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_filename(name)
        if scraper:
            has_positions = run_scraper_test(scraper[0])
            assert has_positions, f"Scraper {name} did not add any jobs."


def test_scarper_adds_valid_jobs(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_filename(name)
        if scraper:
            scraper_positions = run_scraper_and_get_positions(scraper[0])
            if any([not position.url or not position.title or not position.location for position in scraper_positions]):
                assert False, f"Scraper {name} added jobs with missing fields."


def test_scraper_adds_non_sanitized_jobs(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_filename(name)
        if scraper:
            scraper_positions = run_scraper_and_get_positions(scraper[0])
            if any([position.title.strip() != position.title for position in scraper_positions]):
                assert False, f"Scraper {name} added jobs with bad titles. (use .strip())"
            if any([position.location.strip() != position.location for position in scraper_positions]):
                assert False, f"Scraper {name} added jobs with bad locations. (use .strip())"
            if any([position.url.strip() != position.url for position in scraper_positions]):
                assert False, f"Scraper {name} added jobs with bad urls. (use .strip())"


def test_scarper_adds_jobs_with_good_url(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_filename(name)
        if scraper:
            scraper_positions = run_scraper_and_get_positions(scraper[0])
            if any([not validate_url(position.link) for position in scraper_positions]):
                assert False, f"Scraper {name} added jobs with bad urls."


def test_scraper_runtime(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_filename(name)
        if scraper:
            start_time = time.time()
            run_scraper_test(scraper[0])
            end_time = time.time()
            assert check_scraper_performance(start_time, end_time), f"Scraper {name} took longer than 90s."
