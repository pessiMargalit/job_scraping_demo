# Jobscraper Demo 🤖🏙️
This project is a demo for a job scraper that scrapes jobs from different companies and sites.

# Table of Contents
1. [Prerequisites](#prerequisites)
2. [Scrapers](#scrapers)
    1. [Creating new scrapers](#creating-new-scrapers)
    2. [Running the scrapers](#running-the-scrapers)
3. [Authors](#authors)
4. [License](#license)
5. [Acknowledgments](#acknowledgments)




## Prerequisites

Install Python 3.10 or higher.
check the requirements.txt file for the required packages.
and run the following command to install them:
```
pip install -r requirements.txt
```

## Scrapers
### Creating new scrapers
Under the `Scrapers` folder you can find the Abstract classes (such as `Scraper`), and the next folder:
`CompanyScrapers` - contains the scrapers of the companies.

Every scraper is written by the same pattern:
```python
# exampleScraper.py
from Scrapers.Scraper import *


class exampleScraper(Scraper):
    name = 'exampleScraper'
    url = 'example.com'
    location = 'example' # default location, when not set its automatically 'Jerusalem'

    def scrape(self):
        # This is where you will write your logic to scrape the site example.com.
        pass
```

### Running the scrapers
To run a specific scraper you can just add `check_self()` to the end of the file, for example:
```python
# exampleScraper.py
from Scrapers.Scraper import *

class exampleScraper(Scraper):
...
# Same code as above

# This is the line you need to add to run the scraper:
exampleScraper().check_self()
```

Then you can run the file, and it will run the scraper and print the results.

## Authors

* **Snir Sharristh** - *Developer* - [Snirsh](https://github.com/Snirsh)

## License

This project is licensed to Freshboard.city Company.
