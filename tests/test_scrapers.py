import time

import pytest
from Scrapers.ScrapersFactory import ScrapersFactory
from test_utils import run_scraper_test, check_scraper_performance, run_scraper_and_get_positions, validate_url


@pytest.fixture(scope="session")
def factory():
    return ScrapersFactory()


@pytest.fixture(scope="session")
def company_scraper_names(request):
    return request.config.getoption("--companies").split(",")


@pytest.mark.parametrize("company_scraper_name", company_scraper_names)
def pytest_generate_tests(metafunc):
    if 'company_scraper' in metafunc.fixturenames:
        factory = ScrapersFactory()
        company_names = metafunc.config.getoption("--companies")
        scrapers = [factory.get_scraper_by_filename(name) for name in company_names.split(",")] if company_names else []
        metafunc.parametrize("company_scraper", scrapers)


def test_specific_company(factory, company_scraper):
    assert company_scraper, "No company was given"


def test_scraper_name(factory, company_scraper):
    assert company_scraper.name, f"Scraper does not have a name."


def test_scraper_url(factory, company_scraper):
    assert company_scraper.url, f"Scraper {company_scraper.name} does not have a default url."

def test_scarper_adds_valid_jobs(factory, company_scraper):
    start_time = time.time()
    scraper_positions = run_scraper_and_get_positions(company_scraper)
    end_time = time.time()
    name = company_scraper.name
    if any([not position.link or not position.title or not position.location for position in scraper_positions]):
        assert False, f"Scraper {name} added jobs with missing fields."
    if any([position.title.strip() != position.title for position in scraper_positions]):
        assert False, f"Scraper {name} added jobs with bad titles. (use .strip())"
    if any([position.location.strip() != position.location for position in scraper_positions]):
        assert False, f"Scraper {name} added jobs with bad locations. (use .strip())"
    if any([position.link.strip() != position.link for position in scraper_positions]):
        assert False, f"Scraper {name} added jobs with bad urls. (use .strip())"
    if any([not validate_url(position.link) for position in scraper_positions]):
        assert False, f"Scraper {name} added jobs with bad urls (should start with http)."
    assert check_scraper_performance(start_time, end_time), f"Scraper {name} took longer than 90s."
