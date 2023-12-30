from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseCompany import GreenhouseCompany
from ScrapingTools.OutsourceTools.Greenhouse.GreenhouseURLsHandler import GreenhouseURLsHandler

if __name__ == "__main__":
    cuh = GreenhouseURLsHandler()
    # companies_dict = cuh.perform_urls_handler_flow()
    companies_dict = cuh.initialize_company_dict(r"C:\Users\User\Downloads\1.xlsx")
    # cc_general = GreenhouseCompany("")
    # cc_general.checkout_branch(cc_general.branch_name)
    for name, url in companies_dict.items():
        cc = GreenhouseCompany(name, url)
        file_path = cc.generate_scraper()
        cc.add_commit_push(file_path, cc.branch_name)
    # cc_general.checkout_previous_branch()
