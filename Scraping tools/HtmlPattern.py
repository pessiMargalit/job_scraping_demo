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
             "Project", "Manager", "Backend"}


def main():
    url = 'https://www.google.com/about/careers/applications/jobs/results/'
    driver = selenium_url_maker(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(find_by_table(soup))
    print(find_by_list(soup))
    print(get_jobs_info(soup))

def find_by_table(html):
    table = html.findAll("table")
    if table is None:
        return "this html not use with table"
    for t in table:
        tbody = t.find("tbody") if t.find("tbody") else t
        tr = tbody.find("tr")
        if tr:

            splice = splice_tr(tr)
            all_tr = tbody.findAll("tr", recursive=False)

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
    list = html.findAll("ul")
    if len(list) == 0:
        return "this html not use with list"
    for ul in list:
        li = ul.find("li")
        if li:

            splice = splice_tr(li)
            all_li = ul.findAll("li", recursive=False)

            li_class = find_class(splice, all_li)

            if li_class is None:
                li_class = find_parent_class(li)
            for li in all_li:
                str_li = str(li)
                for key in KEY_WORDS:
                    if key in str_li:
                        return li_class

    return None


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
            return str(parent_class[0])
        else:
            return find_parent_class(parent)
    else:
        return None

def get_jobs_info(html):

    class_jobs = find_by_list(html)
    key, value = class_jobs.split('=')
    jobs_arr=[]

    for li in html.findAll('li', {key: value.strip('"')}):
        tr = str(li)



        pattern = r'>([^<]+)<'
        matches = re.findall(pattern, tr)
        jobs_arr.append(matches)
        
        # jobs_arr.append(li.getText())

    return jobs_arr




if __name__ == "__main__":
    main()
