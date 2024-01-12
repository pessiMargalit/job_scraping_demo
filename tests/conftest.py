import pytest

from Scrapers.ScrapersFactory import ScrapersFactory


def pytest_addoption(parser):
    parser.addoption("--companies", action="store", default="",
                     help="Specify company names separated by commas for testing")


@pytest.fixture
def company_scrapers(request):
    companies_string = request.config.getoption("--companies")
    companies_list = [name.strip() for name in companies_string.split(',') if name.strip()]

    if not companies_list:
        return None
    sf = ScrapersFactory()
    return list(map(lambda s: sf.get_scraper_by_filename(s), companies_list))
