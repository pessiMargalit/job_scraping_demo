from ScrapingTools.OutsourceTools.Greenhouse.URLsHandler import GreenhouseURLsHandler

if __name__ == "__main__":
    cuh = GreenhouseURLsHandler()
    companies_dict = cuh.perfortm_urls_handler_flow()
    # companies_dict = cuh.initialize_company_dict(r"C:\Users\User\Downloads\greenhouse.xlsx")
    # cc_general = ComeetCompany("")
    # cc_general.checkout_branch(cc_general.branch_name)
    # for name, url in companies_dict.items():
    #     cc = ComeetCompany(name, url)
    #     file_path = cc.generate_scraper()
    #     cc.add_commit_push(file_path, cc.branch_name)
    # cc_general.checkout_previous_branch()
