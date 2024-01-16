from urllib.request import urlopen
from bs4 import BeautifulSoup


def scrape(company_id):
    webpage_url = "https://www.kycisrael.com/companies/"
    url = webpage_url + str(company_id)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    company_english_name = soup.findAll('div', {'class': 'kkyc-search-result-main'})
    for p in soup.findAll('div', {'class': 'kkyc-search-result-main'}):
        company_english_name = p.findNext('h1')
    return company_english_name.text
