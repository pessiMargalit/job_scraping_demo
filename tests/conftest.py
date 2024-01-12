def pytest_addoption(parser):
    parser.addoption("--scraper", action="store", default=None, help="Name of the scraper to test")
