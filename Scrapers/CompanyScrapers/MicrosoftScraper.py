from Scrapers.Scraper import *


class MicrosoftScraper(Scraper):
    name = 'Microsoft'
    url = 'https://careers.microsoft.com/professionals/us/en/l-israel'
    location = 'Redmond, Washington, United States'

    def __init__(self):
        super(MicrosoftScraper, self).__init__()

    def scrape(self):
        cookies = {
            '__CT_Data': 'gpv=9&ckp=tld&dm=microsoft.com&apv_1067_www32=2&cpv_1067_www32=2&rpv_1067_www32=2',
            'JSESSIONID': 'ddf49040-1f64-4013-b33f-565ae954a8a9',
            'VISITED_COUNTRY': 'us',
            'VISITED_LANG': 'en',
            'VISITED_VARIANT': 'professionals',
            'in_ref': '',
            'PLAY_SESSION': '4ea29d64b76d473ce63a34b5f0124fd8c914278d-JSESSIONID=ddf49040-1f64-4013-b33f-565ae954a8a9',
            'AMCVS_EA76ADE95776D2EC7F000101%40AdobeOrg': '1',
            'AMCV_EA76ADE95776D2EC7F000101%40AdobeOrg': '1585540135%7CMCIDTS%7C18836%7CMCMID%7C01008936431843179483652097687791871537%7CMCAAMLH-1628001892%7C6%7CMCAAMB-1628001892%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1627404292s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18841%7CvVersion%7C4.4.0%7CMCCIDH%7C-1401040460',
            'MS0': 'e273788db02b4102924b76b4c21114e6',
            'mbox': 'PC#c3466cffd7444001bd39784222ee3b6f.37_0#1661583791|session#8d0f7705a0a04190b66140c6f6290d96#1627398952',
            'at_check': 'true',
            '_ga': 'GA1.2.1425079298.1627370450',
            '_gid': 'GA1.2.91895098.1627370450',
            'WRUID': '3396419292922128',
            '_cs_id': '648c4af7-76f9-ae88-b4a6-9df4d28d896c.1627371381.1.1627371761.1627371381.1613561419.1661535381462.None.1',
            '_mkto_trk': 'id:157-GQE-382&token:_mch-microsoft.com-1620630164519-70262',
            '_CT_RS_': 'Recording',
            '_mkto_trk_http': 'id:157-GQE-382&token:_mch-microsoft.com-1620630164519-70262',
            '_cs_c': '0',
            'MSCC': 'NR',
            'PHPPPE_GCC': 's',
            '_gcl_au': '1.1.1041122068.1627232708',
            'Per_UniqueID': '17adea0a29f13f-13c680-89ce-17adea0a2a019ae',
            'AAMC_mscom_0': 'AMSYNCSOP%7C411-18841',
            'MC1': 'GUID=21cd8427d95f4fc98ff77623480c3efd&HASH=21cd&LV=202107&V=4&LU=1627232192934',
            'MUID': '27A4D0976A236A980C4BC0C26B886B75',
        }

        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Host': 'careers.microsoft.com',
            'Origin': 'https://careers.microsoft.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
            'Connection': 'keep-alive',
            'Referer': 'https://careers.microsoft.com/professionals/us/en/l-israel',
            'Content-Length': '163',
            'x-csrf-token': '469957ffedc94d02858a73e46e43eedb',
        }

        data = '{"lang":"en_us","deviceType":"desktop","country":"us","ddoKey":"targetedJobs","jobs":true,"size":"500","all_fields":[],"selected_fields":{},"lpKey":["l-l-herzelia"]}'

        response = requests.post('https://careers.microsoft.com/professionals/widgets', headers=headers,
                                 cookies=cookies, data=data)

        jobs_array = response.json().get('targetedJobs').get('data').get('jobs')

        for job in jobs_array:
            title = job.get('title')
            locations = job.get('multi_location')
            link = f"https://careers.microsoft.com/professionals/us/en/job/{job.get('jobId')}/"
            for location in locations:
                new_title = title
                if len(locations) > 1:
                    new_title = f"{title} ({location})"
                self._company_positions.append(
                    self.Position(
                        title=new_title,
                        link=link,
                        location=location,
                        tags=job.get('category')
                    )
                )
