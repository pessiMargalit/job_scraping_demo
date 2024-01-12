import pytest
import time
from Scrapers.ScrapersFactory import ScrapersFactory
from test_utils import run_scraper_test, check_scraper_performance


@pytest.fixture(scope="session")
def factory():
    return ScrapersFactory()


@pytest.fixture
def company_name(request):
    return request.config.getoption("--company")


def pytest_addoption(parser):
    parser.addoption("--company", action="store", default=None, help="Specify a company name for testing")


def test_specific_company(factory, company_name):
    assert company_name, "No company name was given"


def test_scraper_existence(factory, company_name):
    scraper = factory.get_scraper_by_name(company_name)[0]
    assert scraper, f"Scraper for {company_name} does not exist."


def test_scarper_adds_jobs(factory, company_name):
    scraper = factory.get_scraper_by_name(company_name)[0]
    has_positions, end_time = run_scraper_test(scraper)
    assert has_positions, f"Scraper {company_name} did not add any jobs."

def test_scraper_runtime(factory, company_name):
    scraper = factory.get_scraper_by_name(company_name)[0]
    start_time = time.time()
    scraper.scrape()
    end_time = time.time()
    assert check_scraper_performance(start_time, end_time), f"Scraper {company_name} took longer than 1 minute."