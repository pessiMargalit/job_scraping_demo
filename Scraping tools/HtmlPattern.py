import pandas as pd
from selenium.common import WebDriverException

from Scrapers.Scraper import *
from bs4 import BeautifulSoup

KEY_WORDS = {"Technology", "Innovation", "Research", "Development", "R&D", "Engineering", "Software", "Hardware",
             "Digital", "Cybersecurity", "Cloud Computing", "Data Analysis", "Machine Learning",
             "Artificial Intelligence", "AI", "Internet of Things", "IoT", "Blockchain", "Virtual Reality ", "VR",
             "Augmented Reality", "AR", "Robotics", "Automation", "5G", "Quantum Computing", "User Experience ", "UX",
             "User Interface", "UI", "Software Engineer", "Developer", "Develop", "Data Scientist", "Product Manager",
             "UX", "UI", "Designer", "DevOps", "Engineer", "Cybersecurity Analyst", "Network", "Systems Administrator",
             "Cloud Architect", "AI Specialist", "Machine Learning Engineer", "Full Stack", "Mobile App", "Web",
             "Hardware", "IT", "Consultant", "Technical Support Specialist", "Business Analyst", "QA", "Tester",
             "Project", "Manager", "Management", "Backend", "Nested Table", "Analyst", "Engineer", "Customer Support",
             "Communication", "Consumer"}


def main():
    url = 'https://careers.clarivate.com/search/searchjobs'
    driver = selenium_url_maker(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(find_by_table(soup))
    # print(find_by_list(soup))
    # urls()


def urls():
    excel_file_path = 'url.xlsx'
    df = pd.read_excel(excel_file_path)
    url_column = 'URL'
    result_column1 = 'Result list'
    result_column2 = 'Result table'
    if result_column1 not in df.columns:
        df[result_column1] = ''
    if result_column2 not in df.columns:
        df[result_column2] = ''

    filtered_urls = df[df[url_column].str.lower().str.contains('linkedin') == False]
    sliced_urls = filtered_urls.iloc[40:60]  # Select rows from 1 to 100

    for index, row in sliced_urls.iterrows():
        url = row[url_column]
        try:
            driver = selenium_url_maker(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # Call your processing function here (replace process_function with your actual function)
            # result_list = find_by_list(soup)
            result_table = find_by_table(soup)
            # Update the 'Result' column with the result
            # df.at[index, result_column1] = result_list
            df.at[index, result_column2] = result_table
            print(f"URL at index {index}: {url}")
            print("-" * 30)
        except requests.exceptions.RequestException as e:
            print(f"Error processing URL at index {index}: {e}")

        # Save the updated DataFrame to the Excel file
    df.to_excel(excel_file_path, index=False)


def find_by_table(html):
    tables = html.findAll("table")
    if not tables:
        print("There is no table")
        return "There is no table"
    for table in tables:
        tbody = table.find("tbody") if table.find("tbody") else table
        tr = tbody.find("tr")
        if tr:
            splice = splice_tr(tr)
            print(splice)
            all_tr = tbody.findAll("tr")
            tr_class = find_class(splice, all_tr)
            if tr_class is None:
                tr_class = find_parent_class(tr)
            for tr in all_tr:
                str_tr = str(tr)
                for key in KEY_WORDS:
                    if key in str_tr:
                        return tr_class
    return None


def find_by_list(html):
    li_class = None
    list = html.findAll("ul")
    if not list:
        print("There is no in list")
        return "There is no in list"
    for ul in list:
        found_ul_with_keywords = False
        all_li = ul.findAll("li", recursive=False)
        for li in all_li:
            ul_contains_keyword = any(keyword in str(li) for keyword in KEY_WORDS)
            if not ul_contains_keyword:
                break
        else:
            found_ul_with_keywords = True
        if found_ul_with_keywords:
            li1 = ul.find("li")
            if li1:
                splice = splice_tr(li1)
                all_li = ul.findAll("li", recursive=False)
                li_class = find_class(splice, all_li)
                if li_class is None:
                    li_class = find_parent_class(li1)
                break
    if li_class is None:
        print("the jobs are not in list")
        return "the jobs are not in list"
    print(li_class)
    return li_class


def selenium_url_maker(url, debug=False, ssl_problems=False):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    if not debug:
        chrome_options.add_argument("--headless")
    if ssl_problems:
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--allow-insecure-localhost")
        chrome_options.add_argument("--ignore-urlfetcher-cert-requests")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver


def find_class(tr, arr_tr):
    for string1 in tr:
        if all(string1 in str(string2) for string2 in arr_tr):
            return string1
    return None


def splice_tr(tr):
    tr = str(tr)
    pos = tr.find('>')
    # Extract the substring up to the first '>'
    substring_until_gt = tr[:pos + 1] if pos != -1 else tr
    pattern = r'([\w-]+\s*=\s*\"[^\"]+\")'
    matches = re.findall(pattern, substring_until_gt)
    return matches


def find_parent_class(element):
    if element is None:
        return None
    parent = element.find_parent()
    if parent:
        element_type = parent.name
        parent_class = splice_tr(parent)
        if parent_class:
            # print(type(parent_class[0]))
            return parent_class[0]
        else:
            return find_parent_class(parent)
    else:
        return None


if __name__ == "__main__":
    main()
