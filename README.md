<div>
  <h2 style="margin-left: 10px;"><b>Freshboard GitHub Repository</b></h2>
  <img src="Freshboard.png" alt="Logo" style="width: 50px; height: auto;">
</div>

## 📚 Table of Contents
1. [Overview](#-overview)
2. [Prerequisites](#-prerequisites)
3. [Implementation Details](#-implementation-details)
4. [Workflow and Process Overview](#-workflow-and-process-overview)
5. [Examples Usage](#-example-usage)
   1. [Mapping Directly With URL Searcher](#mapping-directly-with-url-searcher)
   2. [Mapping With Excel Handler](#mapping-with-excel-handler)
   3. [Mapping Outsource Careers URLs](#mapping-outsource-careers-urls)
   4. [Generating Outsource Scraper](#generating-outsource-scraper)
   5. [Creating New Scraper](#creating-new-scraper)
   6. [Running The Scrapers](#running-the-scrapers)
7. [Testing Flow](#-testing-flow)
8. [Future Enhancements](#-future-enhancements)
9. [Conclusion](#-conclusion)

## 🌐 Overview
JLM Freshboard is a pioneering Jerusalem start-up, revolutionizing job search by developing a comprehensive job board for the Jerusalem Municipality. Our platform aggregates all open positions across various fields in Jerusalem, updated daily and sourced directly from company websites. This ensures real-time availability of opportunities, unlike traditional job sites.
🔗 https://jlmtech.freshboard.city/

## 💻 Prerequisites

Install Python 3.10 or higher.
check the requirements.txt file for the required packages.
and run the following command to install them:
```
pip install -r requirements.txt
```

## 🔧 Implementation Details
This repository is divided into three main parts:
1. **Mapping Tool**: Utilizes AI, web search, advanced language models, and web scraping to automate the process of finding and verifying official website URLs for companies.
2. **Outsource Scraping Tool**:  Automates the creation of scrapers for companies that use external suppliers for job advertisements, by inheriting from a base scraper designed for each outsourcing company.
3. **Manual Scrapers**: Scrapers for specific companies that use BeautifulSoup, Selenium, Json and HTTP requests.
The scrapers are based on a ready-made scraping infrastructure and are dedicated to the structure of the jobs according to the company's website.

## 🔄 Workflow and Process Overview
The process flow includes:
- **URL Mapping**: Using the Mapping Tool for accurate URL identification.
- **Outsource Scraping**: Automatically generating scrapers for companies using outsourcing services.
- **Manual Scraping**: Deploying custom scrapers for unique company websites.
- **Data Integration**: Merging and managing data from various sources for the job board.

## 📝 Examples Usage
### Mapping Directly With URL Searcher
Details of the implementation and flow process of `UrlSearcher` can be found at [DesignDoc](DesignDoc.md)

```python
from MappingTools import UrlSearcher

# Company details
hebrew_company_name = "החברה"
english_company_name = "The Company"
company_address = "123 Company St., Jerusalem"

url_searcher = UrlSearcher(hebrew_company_name, english_company_name, company_address)
found_url = url_searcher.find_url()
print("Found URL:", found_url)

test_results = url_searcher.test_url(found_url, "Software Development")
print("Accuracy:", test_results)

find_careers = url_searcher.get_career_url(found_url)
print("Career page:",find_careers)
```
### Mapping With Excel Handler
To map companies with an Excel file you can use the class `ExcelHandler`.
the function `iterate_rows` receives flags for the process the user wants to perform - URL search, careers page search and the accuracy test.

```python
    file_path = 'your/file_path/career_file.xslx'
    excel_handler = ExcelHandler(file_path)
    # True / False - depends on required actions
    excel_handler.iterate_rows(find_url=True, find_careers=True, get_accuracy=True)
```

### Mapping Outsource Careers URLs
The result of running this code is the list of companies that use a relevant outsourcing company with the URL to each company's careers page
```python
from ScrapingTools.OutsourceTools.Comeet.ComeetURLsHandler import ComeetURLsHandler

url_handler = ComeetURLsHandler()
comeet_companies = url_handler.perform_urls_handler_flow()
```

### Generating Outsource Scraper
Creating a scraper inheriting from the base scraper of the relevant outsourcing company and pushing it to GitHub
```python
from ScrapingTools.OutsourceTools.Comeet.ComeetCompany import ComeetCompany

comeet_company = ComeetCompany(name, url)
# Generates a suitable scraper for the company according to the template of the relevant outsourcing
file_path = comeet_company.generate_scraper()
# add, commit and push to the repo in github
comeet_company.add_commit_push(file_path, comeet_company.branch_name)

```
### Creating New Scraper
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
# MobileyeScraper.py

# Example of using a specific scraper
from Scrapers.Scraper import *

class MobileyeScraper(Scraper):
...
# Same code as above

scraper = MobileyeScraper()
# This is the line you need to add to run the scraper:
scraper.check_self()

# output:
--------------------------------------------------
Title: HRBP
Company: Mobileye
Location: Jerusalem, Israel
Link: https://careers.mobileye.com/jobs/hrbp/0f0816ae-3c12-4c75-a35a-f4db3e0f288c
--------------------------------------------------
Title: Talent Acquisition Partner
Company: Mobileye
Location: Jerusalem, Israel
Link: https://careers.mobileye.com/jobs/talent-acquisition-partner/ecaed4c9-7943-4283-b1e9-1946773d43a4
--------------------------------------------------
Total: 137

```


## 🧪 Testing Flow
- Comprehensive tests are conducted for all scrapers, including those for outsourcing.
- Testing is mandatory for each Pull Request (PR) to ensure scraper integrity.
- `test_scrapers.py` script is used for testing purposes.
- `TestURL.py` is used for URL validation and accuracy.
  
## 🚀 Future Enhancements
- Enhanced AI capabilities for more accurate job mapping.
- Scaling to include other cities and regions.
- Continuous improvement through user feedback and technological advancements.

## 🎉 Conclusion
At JLM Freshboard, we're dedicated to making job searching in Jerusalem as comprehensive and user-friendly as possible. Contributions, suggestions, and feedback are highly appreciated to help us evolve and expand our services.

## 👨‍💻 Authors

* **Snir Sharristh** - *Chief Software Engineer* - [Snirsh](https://github.com/Snirsh)
* **Brachi Malmud** - *Team Lead* -  [BrachiMalmud](https://github.com/Brachi-Melamud)
* **Shani Shurkin** - *Backend and Web Scraping Developer* - [ShaniShurkin](https://github.com/ShaniShurkin)
* **Pessi Margalit** - *Backend and Web Scraping Developer* - [pessiMargalit](https://github.com/pessiMargalit)
* **Chavi Daitsh** - *Backend and Web Scraping Developer* - [ChaviDaitsh](https://github.com/ChaviDaitsh)
* **Yeudit Hazan** - *Backend and Web Scraping Developer* - [YehuditShrg](https://github.com/YehuditShrg)
* **Chani Rosental** - *Backend and Web Scraping Developer* - [ChanyRosental](https://github.com/ChanyRosental)
* **Ruti Bergshtain** - *Backend and Web Scraping Developer* - [RutiB](https://github.com/Ruti742)
* **Chani Ortal** - *Backend and Web Scraping Developer* - [ChaniOrtal](https://github.com/seminar0533131761)
 

## 📜 License

This project is licensed to Freshboard.city Company.

