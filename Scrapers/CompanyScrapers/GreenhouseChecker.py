import requests


def check_for_greenhouse(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (HTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        print('0')
        response = requests.get(url, headers=headers)
        print("1")
        response.raise_for_status()  # Raise an exception for bad responses
        print('2')
        response = requests.get(url)
        print(response.text)
    #     if response.status_code == 200:
    #         page_content = response.text
    #
    #         # Check for specific identifiers or URLs associated with Greenhouse
    #         if 'greenhouse.io' in page_content:
    #             print("This site seems to be using Greenhouse.")
    #         else:
    #             print("Greenhouse not detected on this site.")
    #     else:
    #         print("Failed to fetch the webpage. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error fetching the webpage:", e)


# Replace 'url_here' with the URL of the site you want to check
url = 'https://www.axonius.com/company/careers/open-jobs'
check_for_greenhouse(url)
