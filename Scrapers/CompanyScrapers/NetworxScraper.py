from urllib.parse import urljoin

from Scrapers.Scraper import *


class NetworxScraper(Scraper):
    name = 'networx'
    url = 'https://apply.workable.com/networx-1/'

    def scrape(self):
        headers = {
            'authority': 'apply.workable.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            # 'cookie': 'wmc=%7B%22cookie_id%22%3A%22db4ac5c6-8822-413f-977d-5810303b93dc%22%7D; __cf_bm=vNKn.eUVEa9hWU8yDFyZtX_C8oTR6XoUDJEqOyN.uLo-1705937619-1-AYQNO0es3nqR1Kmb9yvYGxXCbJquDV6qvdDlpjYXv/tOfVFDfJvv1UGt7baovuI3LjaDFTth3DpmkQ3E9X1mlo8=; _gid=GA1.2.1690116493.1705937621; _hjIncludedInSessionSample_1398434=0; _hjSession_1398434=eyJpZCI6IjUxZTViMzQ0LWMzYzYtNDQxMi1hNzc5LTAwNTk3N2VhZjE1OCIsImMiOjE3MDU5Mzc2MjE1ODEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _hjSessionUser_1398434=eyJpZCI6IjRlMDU4YmQ4LTQzZGItNTE2NS05ODAxLTFjMzkzMGI4N2NhZSIsImNyZWF0ZWQiOjE3MDU5Mzc2MjE1ODAsImV4aXN0aW5nIjp0cnVlfQ==; _ga_L9T8SS12Q7=GS1.1.1705937620.1.1.1705938210.0.0.0; _ga=GA1.2.782863006.1705937621; _gat_UA-135782126-1=1; _dd_s=rum=0&expire=1705939113389',
            'origin': 'https://apply.workable.com',
            'pragma': 'no-cache',
            'referer': 'https://apply.workable.com/networx-1/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }

        json_data = {
            'query': '',
            'location': [],
            'department': [],
            'worktype': [],
            'remote': [],
            'workplace': [],
        }

        response = requests.post(
            'https://apply.workable.com/api/v3/accounts/networx-1/jobs',
            headers=headers,
            json=json_data,
        )
        jobs_json = response.json()
        for job in jobs_json.get('results'):
            self.positions.append(
                self.Position(
                    title=job.get('title'),
                    link=f"https://apply.workable.com/networx-1/j/{job.get('shortcode')}/",
                    location=f"{job.get('location').get('country')}, {job.get('location').get('city')}",
                    remote=job.get('remote')
                )
            )
