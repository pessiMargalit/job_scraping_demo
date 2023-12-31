from ScrapingTools.OutsourceTools.Comeet.ComeetURLsHandler import ComeetURLsHandler
from ScrapingTools.OutsourceTools.Comeet.ComeetCompany import ComeetCompany

if __name__ == "__main__":
    cuh = ComeetURLsHandler()
    # companies_dict = cuh.perform_urls_handler_flow()
    # print(companies_dict)
    companies_dict = cuh.initialize_company_dict(r"C:\Users\user\Downloads\comeetBSD.xlsx")
    cc_general = ComeetCompany("", "")
    cc_general.checkout_branch(cc_general.branch_name)
    for name, url in companies_dict.items():
        cc = ComeetCompany(name, url)
        file_path = cc.generate_scraper()
        cc.add_commit_push(file_path, cc.branch_name)
    cc_general.checkout_previous_branch()
