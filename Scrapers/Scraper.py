"""
This is the main scraper class, an "abstract" (not via abc library currently), that all the scrapers will inherit from.
"""
from math import cos, pi, floor
from os import getenv
from typing import NamedTuple
from urllib.request import urlopen
from urllib import error, parse
from urllib.request import build_opener
from bs4 import BeautifulSoup
from selenium import webdriver
import ssl
from Scrapers.PositionClass import *
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.chrome.service import Service
import time
import requests
import json
from datetime import datetime
from Scrapers.PositionClass import PositionClass

HTML_PARSER = 'html.parser'

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/88.0.705.74"
]


class Scraper:
    """
    The main Scraper 'abstract' class
    """

    location = 'Jerusalem'  # Default, the city of all cities ;)

    def __init__(self):
        """
        initialize a new scraper that has a default Positions list that is of type:
        positions = (Position_object1, ...)
        where Position_object is Position object type that is of the following:

        Position(title= '', company=defaulted to the scrapers self.name, link=defaulted to the scrapers self.url)

        Please consider the objects defaults!
        """
        self.positions = []
        self.pos_class = PositionClass(
            defaults=(None, self.name, self.url, self.location, False, None, None, FULLTIME_JOB, None, '')
        )
        self.Position = self.pos_class.create_position

    def get_positions(self):
        """
        :return: the list of positions that had been(or not) scraped
        """
        return self.positions

    def scrape(self):
        """
        this should be implemented by each scraper
        :return:
        """
        raise NotImplementedError("No scraper was implemented!")

    @staticmethod
    def selenium_url_maker(url, debug=False, ssl_problems=False):
        """
        this method creates a selenium webdriver that will be used to scrape via chrome simulator
        :param url: the url we want to scrape
        :param debug: if True then Chrome wont be headless! meaning you will see what selenium sees
        :param ssl_problems: if there are any ssl problems (mostly there aren't), try this
        :return: returns a chrome webdriver according to the parameters given
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-dev-shm-usage')
        if not debug:
            chrome_options.add_argument("--headless")
        if ssl_problems:
            chrome_options.add_argument("--allow-running-insecure-content")
            chrome_options.add_argument("--allow-insecure-localhost")
            chrome_options.add_argument("--ignore-urlfetcher-cert-requests")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        return driver

    @staticmethod
    def scraping_unit(page_url):
        try:
            page = urlopen(page_url)
            return BeautifulSoup(page, HTML_PARSER)
        except error.HTTPError as e:
            if e.code == 404:
                return
            opener = build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
            page = opener.open(page_url)
            return BeautifulSoup(page, HTML_PARSER)
        except ssl.CertificateError:
            ssl.match_hostname = lambda cert, hostname: True
            page = urlopen(page_url)
            return BeautifulSoup(page, HTML_PARSER)
        except error.URLError:
            context = ssl._create_unverified_context()
            page = urlopen(page_url, context=context)
            return BeautifulSoup(page, HTML_PARSER)

    def check_self(self, content=False, location='', title='', link=''):
        self.scrape()
        if content:
            pos_to_print = [
                {'title': p.title, 'company': p.company, 'location': p.location, 'link': p.link, 'content': p.content}
                for p in self.positions]
        else:
            pos_to_print = [{'title': p.title, 'company': p.company, 'location': p.location, 'link': p.link} for p in
                            self.positions]
        if location:
            pos_to_print = [p for p in pos_to_print if location in p['location']]
        if title:
            pos_to_print = [p for p in pos_to_print if title in p['title']]
        if link:
            pos_to_print = [p for p in pos_to_print if link in p['link']]
        for p in pos_to_print:
            if content:
                print(
                    "Title: {title}\nCompany: {company}\nLocation: {location}\nLink: {link}\nContent: {content}".format(
                        **p))
            else:
                print("Title: {title}\nCompany: {company}\nLocation: {location}\nLink: {link}".format(**p))
            print("--------------------------------------------------")
        if len(pos_to_print):
            print(f"Total: {len(pos_to_print)}")
        else:
            print("No positions were found")

    @staticmethod
    def get_challenge_answer(challenge):
        """
        Solve the math part of the challenge and get the result
        """
        arr = list(challenge)
        last_digit = int(arr[-1])
        arr.sort()
        min_digit = int(arr[0])
        subvar1 = (2 * int(arr[2])) + int(arr[1])
        subvar2 = str(2 * int(arr[2])) + arr[1]
        power = ((int(arr[0]) * 1) + 2) ** int(arr[1])
        x = (int(challenge) * 3 + subvar1)
        y = cos(pi * subvar1)
        answer = x * y
        answer -= power
        answer += (min_digit - last_digit)
        answer = str(int(floor(answer))) + subvar2
        return answer

    @staticmethod
    def parse_challenge(page):
        top = page.split('<script>')[1].split('\n')
        challenge = top[1].split(';')[0].split('=')[1]
        challenge_id = top[2].split(';')[0].split('=')[1]
        return {'challenge': challenge, 'challenge_id': challenge_id,
                'challenge_result': Scraper.get_challenge_answer(challenge)}

    @staticmethod
    def solve_challenge(URL):
        s = requests.Session()
        r = s.get(URL)

        if 'X-AA-Challenge' in r.text:
            challenge = Scraper.parse_challenge(r.text)
            r = s.get(URL, headers={
                'X-AA-Challenge': challenge['challenge'],
                'X-AA-Challenge-ID': challenge['challenge_id'],
                'X-AA-Challenge-Result': challenge['challenge_result']
            })

            yum = r.cookies
            r = s.get(URL, cookies=yum)
        return r

    @staticmethod
    def quote_url(url):
        return parse.quote(url, safe=':/?&')

    @staticmethod
    def hebrew_split(s):
        s = s.replace(',', ' , ')
        words = s.split(' ')
        segments = []
        current_segment = ""

        for i, word in enumerate(words):
            # Handling the first word
            if i == 0:
                current_segment += word
                # Handling ","
            elif word == ",":
                segments.append(current_segment.strip())
                current_segment = ""
                # Handling "וגם"
            elif word == "וגם":
                segments.append(current_segment.strip())
                current_segment = ""
                # Handling words that begin with 'ו'
            elif word.startswith('ו'):
                segments.append(current_segment.strip())
                current_segment = word[1:]  # Removing the 'ו' at the beginning
                # Handling other words
            else:
                if current_segment:
                    current_segment += " " + word
                else:
                    current_segment += word

        # Appending the last segment
        if current_segment:
            segments.append(current_segment.strip())

        return segments