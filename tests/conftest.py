import pytest


def pytest_addoption(parser):
    parser.addoption("--companies", action="store", default="",
                     help="Specify company names separated by commas for testing")


@pytest.fixture
def company_names(request):
    companies_string = request.config.getoption("--companies")
    companies_list = [name.strip() for name in companies_string.split(',') if name.strip()]

    if not companies_list:
        pytest.fail("No company names were provided with --companies argument")

    return companies_list
