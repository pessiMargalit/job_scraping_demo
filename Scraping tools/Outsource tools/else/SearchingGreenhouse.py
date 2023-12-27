from SearchingURLs import *


class GreenhouseSearcher(UrlSearcher):
    companies = ['MESH Payments', 'AppsFlyer', 'Codefresh', 'Meetup', 'Similarweb', 'Vareto', 'Axonius', 'Torii',
                 'Chronosphere', 'Placer.ai', 'DoubleVerify', 'Seccl', 'MyHeritage', 'Bluevine', 'Nomad Health',
                 "Tally",
                 'Protocol Labs', 'Redis Labs', 'DeepMind', 'Redpanda', 'Forter', 'Plarium', 'Gong.io', 'Maven Clinic',
                 'Vimeo', 'Snyk', 'Sisense', 'NICE Systems Ltd', 'SOUTHWORKS', 'Valera Health', 'Melio', 'Riskified',
                 'Tipalti', 'Perion', 'OwnBackup', 'Cato Networks', 'OpenAI', 'Lightricks', 'Liveperson', 'SentinelOne',
                 'Handshake', 'Outbrain', 'Simply', 'Hillel', 'Gamida Cell', 'Pagaya', 'WeWork', 'Pax8', 'Blinkist',
                 'Unity', 'JFrog']

    @staticmethod
    def get_first_google_result(company_name, query):
        super().get_first_google_result(company_name, query)

    def write_urls_to_excel(self, file):
        # Read the Excel file
        df = pd.DataFrame({'Company Name': self.companies})

        # Create a new column for the URLs
        df['Link To Website'] = df['Company Name'].apply(GreenhouseSearcher.get_first_google_result, args='career')
        df['Link To Greenhouse Website'] = df['Company Name'].apply(GreenhouseSearcher.get_first_google_result,
                                                                    args='greenhouse')
        # Retry for timed-out queries
        retries = 3
        for i in range(retries):
            try:
                # Save the updated DataFrame to a new Excel file
                df.to_excel(file, index=False, engine='openpyxl')
                print("File updated successfully.")
                break
            except TimeoutError:
                print(f"TimeoutError: Retry {i + 1}/{retries}. Waiting for 5 seconds.")
                time.sleep(5)
                continue
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")
                break


# # Replace 'input_file.xlsx' and 'output_file.xlsx' with your actual file names
GreenhouseSearcher.write_urls_to_excel('../Careers files/greenhouse.xlsx')
