import requests
import json

url = 'https://careers.clarivate.com/search/searchresults?jtStartIndex=12&jtPageSize=12'

headers = {
    '__requestverificationtoken': 'hYWYrflrKZifXlxVRgnq9i-5BPGVQ1QqFbpN5uIZjjw-WKw6utetZHWHdyOn6XM73WeO6lSeavaDX4b3Yc5yOKA2g2I1',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-requested-with': 'XMLHttpRequest'
}

body = {
    'Keyword': '',
    'ClientID': '00000000-0000-0000-0000-000000000000',
    'IndustryID': '',
    'FamilyID': '',
    'CategoryID': '',
    'AdTypeID': '',
    'AdShiftID': '',
    'AdScheduleID': '',
    'AdSalaryID': '',
    'AdDepartmentID': '',
    'FacilityID': '',
    'CityState': '',
    'GeolocationString': '',
    'Radius': '15',
    'BrandName': '',
    'FacilityIDs': '',
    'FacilityName': '',
    'RegionalState': '',
    'RegionalCountry': '',
    'StateCountry': '',
    'CountryOnly': '',
    'PostedDate': '',
    'FeaturedOnly': 'False',
    'FeaturedGID': '',
    'RemoteJobs': 'False'
}

response = requests.get(url, headers=headers, data=body)

if response.status_code == 200:
    jobs_data = response.json()
    print(json.dumps(jobs_data, indent=4))
else:
    print(f"Failed to fetch jobs. Status code: {response.status_code}")
