# conftest.py (continued)
import pytest

def pytest_addoption(parser):
    parser.addoption("--company", action="store", default=None, help="Specify a company name for testing")

@pytest.fixture
def company_name(request):
    return request.config.getoption("--company")
