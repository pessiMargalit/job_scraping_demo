import time

import pytest
from Scrapers.ScrapersFactory import ScrapersFactory
from test_utils import run_scraper_test, check_scraper_performance, run_scraper_and_get_positions, validate_url


@pytest.fixture(scope="session")
def factory():
    return ScrapersFactory()


# In your test file
@pytest.fixture(scope="session")
def company_scraper(request, factory):
    scraper_name = request.config.getoption("--scraper")
    if scraper_name:
        return factory.get_scraper_by_filename(scraper_name)


def test_specific_company(factory, company_scraper):
    assert company_scraper, "No scrapers were given"


def test_scraper_name(factory, company_scraper):
    assert company_scraper.name, f"Scraper does not have a name."


def test_scraper_url(factory, company_scraper):
    assert company_scraper.url, f"Scraper {company_scraper.name} does not have a default url."


def test_scarper_adds_jobs(factory, company_scraper):
    has_positions = run_scraper_test(company_scraper)
    assert has_positions, f"Scraper {company_scraper.name} did not add any jobs."


def test_scarper_adds_valid_jobs(factory, company_scraper):
    scraper_positions = run_scraper_and_get_positions(company_scraper)
    if not scraper_positions:
        assert False, f"Scraper {company_scraper.name} did not add any jobs."
    if any([not position.url or not position.title or not position.location for position in scraper_positions]):
        assert False, f"Scraper {company_scraper.name} added jobs with missing fields."


def test_scraper_adds_non_sanitized_jobs(factory, company_scraper):
    name = company_scraper.name
    scraper_positions = run_scraper_and_get_positions(company_scraper)
    if not scraper_positions:
        assert False, f"Scraper {company_scraper.name} did not add any jobs."
    if any([position.title.strip() != position.title for position in scraper_positions]):
        assert False, f"Scraper {name} added jobs with bad titles. (use .strip())"
    if any([position.location.strip() != position.location for position in scraper_positions]):
        assert False, f"Scraper {name} added jobs with bad locations. (use .strip())"
    if any([position.url.strip() != position.url for position in scraper_positions]):
        assert False, f"Scraper {name} added jobs with bad urls. (use .strip())"


def test_scarper_adds_jobs_with_good_url(factory, company_scraper):
    name = company_scraper.name
    scraper_positions = run_scraper_and_get_positions(company_scraper)
    if not scraper_positions:
        assert False, f"Scraper {company_scraper.name} did not add any jobs."
    if any([not validate_url(position.link) for position in scraper_positions]):
        assert False, f"Scraper {name} added jobs with bad urls."


def test_scraper_runtime(factory, company_scraper):
    name = company_scraper.name
    start_time = time.time()
    scraper_positions = run_scraper_test(company_scraper)
    end_time = time.time()
    if not scraper_positions:
        assert False, f"Scraper {company_scraper.name} did not add any jobs."
    assert check_scraper_performance(start_time, end_time), f"Scraper {name} took longer than 90s."
