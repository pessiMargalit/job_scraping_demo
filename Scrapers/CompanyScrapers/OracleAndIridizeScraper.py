from Scrapers.Scraper import *


class OracleAndIridizeScraper(Scraper):
    name = 'Oracle'
    base_url = 'https://careers.oracle.com/jobs/#en/sites/jobsearch/requisitions'
    url = 'https://eeho.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?' \
          'onlyData=true&expand=requisitionList.secondaryLocations,flexFieldsFacet.values&finder=findReqs;' \
          'siteNumber=CX_45001,facetsList=LOCATIONS%3BWORK_LOCATIONS%3BWORKPLACE_TYPES%3BTITLES%3BCATEGORIES%3B' \
          'ORGANIZATIONS%3BPOSTING_DATES%3BFLEX_FIELDS,limit=14,locationId=300000000106941,sortBy=POSTING_DATES_DESC'
    location = 'Jerusalem'

    def scrape(self):
        all_jobs_response = requests.get(self.url)
        if all_jobs_response.status_code == 200:
            data = all_jobs_response.json()
            all_jobs_data = data['items'][0]['requisitionList']
            for job in all_jobs_data:
                title = job['Title']
                location = job['PrimaryLocation']
                content = job['ShortDescriptionStr']
                job_id = job['Id']
                self.positions.append(self.Position(
                    title=title.strip() if title else None,
                    link=f'{self.base_url}/preview/{job_id}',
                    location=location.strip() if location else None,
                    content=content.strip() if content else None
                ))
