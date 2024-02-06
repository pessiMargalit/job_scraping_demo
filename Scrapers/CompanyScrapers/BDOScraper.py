import math

import requests
from Scrapers.Scraper import Scraper


class BDOScraper(Scraper):
    name = "BDO"
    url = "https://bdo-career.hunterhrms.com/%D7%9B%D7%9C-%D7%94%D7%9E%D7%A9%D7%A8%D7%95%D7%AA/#page-1"


    @staticmethod
    def get_num_of_json_pg():
        json_url = "https://bdo-career.hunterhrms.com/wp-json/niloosoft/v1/search-results?page="

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "bdo-career.hunterhrms.com",
            "Referer": "https://bdo-career.hunterhrms.com/%D7%9B%D7%9C-%D7%94%D7%9E%D7%A9%D7%A8%D7%95%D7%AA/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "X-WP-Nonce": "24580a7e40",
            "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        response = requests.get(json_url, headers=headers)
        total = response.json()["totalHits"]
        window = response.json()["window"]
        return math.ceil(int(total) / int(window))

    def scrape(self):
        json_url = "https://bdo-career.hunterhrms.com/wp-json/niloosoft/v1/search-results?page="

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "bdo-career.hunterhrms.com",
            "Referer": "https://bdo-career.hunterhrms.com/%D7%9B%D7%9C-%D7%94%D7%9E%D7%A9%D7%A8%D7%95%D7%AA/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "X-WP-Nonce": "24580a7e40",
            "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        for pg_num in range(int(BDOScraper().get_num_of_json_pg())):
            url = f"{json_url}{pg_num - 1}"
            response = requests.get(url, headers=headers)
            jobs = response.json()
            print(jobs)
