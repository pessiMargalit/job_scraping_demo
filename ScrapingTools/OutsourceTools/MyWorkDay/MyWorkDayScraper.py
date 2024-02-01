from Scrapers.Scraper import *
from urllib.parse import urlparse, urlunparse
import asyncio
import aiohttp


class MyWorkDayScraper(Scraper):
    url = 'MyWorkDayMainScraper'
    name = None

    def scrape_widget(self):
        first_response = requests.get(self.url.replace('widgets', ''))
        sessionParams = json.loads(first_response.text.split('phApp.sessionParams = ')[1].split('}')[0] + '}')
        cookies = {'JSESSIONID': first_response.headers['Set-Cookie'].split('JSESSIONID=')[1].split(';')[0]}
        headers = {
            'x-csrf-token': sessionParams['csrfToken'],
        }

        json_data = {
            'lang': 'en_us',
            'deviceType': 'desktop',
            'country': 'us',
            'pageName': 'search-results',
            'ddoKey': 'refineSearch',
            'sortBy': '',
            'subsearch': '',
            'from': 0,
            'jobs': True,
            'counts': True,
            'all_fields': [
                'category',
                'country',
                'state',
                'city',
                'type',
                'postalCode',
                'remote',
            ],
            'size': 500,
            'clearAll': False,
            'jdsource': 'facets',
            'isSliderEnable': False,
            'pageId': 'page11',
            'siteType': 'external',
            'keywords': '',
            'global': True,
            'locationData': {},
        }
        response = requests.post(self.url, headers=headers, cookies=cookies, json=json_data)

        first_json = response.json()
        raw_jobs = first_json.get('refineSearch').get('data').get('jobs')
        data_jsons = []
        for i in range(0, int(first_json.get('refineSearch').get('totalHits')), 500):
            current_json = json_data
            current_json['from'] = i
            data_jsons.append(current_json)
        for j in data_jsons:
            response = requests.post(self.url, headers=headers, cookies=cookies, json=j)
            raw_jobs.extend(response.json().get('refineSearch').get('data').get('jobs'))

        for job in raw_jobs:
            locations = job.get('multi_location') or [job.get('location')]
            if len(locations) == 1:
                self.positions.append(
                    self.Position(
                        title=job.get('title'),
                        link=job.get('applyUrl').replace('/apply', '/'),
                        location=locations[0],
                    )
                )
            else:
                for location in locations:
                    self.positions.append(
                        self.Position(
                            title=f"{job.get('title')} ({location})",
                            link=job.get('applyUrl').replace('/apply', '/'),
                            location=location,
                        )
                    )

    def scrape_external(self):
        json_data = {
            'limit': 20,
            'offset': 0,
        }
        BASE_URL = self.url
        new_url = urlparse(BASE_URL)
        url_parts = BASE_URL.split('/')
        COMPANY_URL = urlunparse((new_url.scheme, new_url.netloc, '/'.join([url_parts[1], url_parts[-2]]), '', '', ''))
        response = requests.post(
            BASE_URL,
            json=json_data,
        )

        raw_json = response.json()
        total = raw_json.get('total')
        json_data_list = [json_data]
        for i in range(20, total, 20):
            json_data_list.append({'limit': 20, 'offset': i})
        loop = asyncio.new_event_loop()
        jsons = loop.run_until_complete(MyWorkDayScraper.get_pages(loop, BASE_URL, json_data_list))
        all_jobs = raw_json.get('jobPostings')
        for j in jsons:
            all_jobs.extend(j.get('jobPostings'))
        for job in all_jobs:
            if (not job.get('title')) or (not job.get('externalPath')):
                continue
            self.positions.append(
                self.Position(
                    title=job.get('title'),
                    link=f"{COMPANY_URL}{job.get('externalPath')}",
                    location=job.get('locationsText'),
                )
            )

    def scrape(self):
        if 'widget' in self.url.lower():
            self.scrape_widget()
        else:
            self.scrape_external()

    @staticmethod
    async def get_page(session, url, data):
        async with session.post(url, json=data) as response:
            return await response.json()

    @staticmethod
    async def get_pages(loop, url, data_list):
        async with aiohttp.ClientSession(loop=loop) as session:
            results = await asyncio.gather(
                *[MyWorkDayScraper.get_page(session, url, data) for data in data_list],
                return_exceptions=True)
            return results