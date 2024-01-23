def pytest_addoption(parser):
    parser.addoption("--companies", action="store", default=None, help="Companies scraper paths to test")