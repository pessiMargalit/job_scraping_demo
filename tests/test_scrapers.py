import time

import pytest
from Scrapers.ScrapersFactory import ScrapersFactory
from test_utils import run_scraper_test, check_scraper_performance


@pytest.fixture(scope="session")
def factory():
    return ScrapersFactory()


@pytest.fixture
def company_names(request):
    companies_string = request.config.getoption("--companies")
    return [name.strip() for name in companies_string.split(',') if name.strip()]


def pytest_addoption(parser):
    parser.addoption("--companies", action="store", default="",
                     help="Specify company names separated by commas for testing")


def test_specific_company(factory, company_names):
    assert company_names, "No company name was given"


def test_scraper_existence(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_name(name)
        assert scraper, f"Scraper {name} does not exist."


def test_scarper_adds_jobs(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_name(name)
        if scraper:
            has_positions, end_time = run_scraper_test(scraper[0])
            assert has_positions, f"Scraper {name} did not add any jobs."


def test_scraper_runtime(factory, company_names):
    for name in company_names:
        scraper = factory.get_scraper_by_name(name)
        if scraper:
            start_time = time.time()
            run_scraper_test(scraper[0])
            end_time = time.time()
            assert check_scraper_performance(start_time, end_time), f"Scraper {name} took longer than 90s."
