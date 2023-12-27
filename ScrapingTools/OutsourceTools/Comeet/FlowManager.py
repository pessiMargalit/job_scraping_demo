from ScrapingTools.OutsourceTools.Comeet.URLsHandler import ComeetURLsHandler
from ScrapingTools.OutsourceTools.Comeet.Company import ComeetCompany

if __name__ == "__main__":
    cuh = ComeetURLsHandler()
    # companies_dict = cuh.perform_urls_handler_flow()
    companies_dict = cuh.initialize_company_dict(r"C:\Users\User\Downloads\res.xlsx")
    for name, url in companies_dict.items():
        cc = ComeetCompany(name, url)
        cc.checkout_branch(cc.branch_name)
        file_path = cc.generate_scraper()
        cc.add_commit_push(file_path, cc.branch_name)
