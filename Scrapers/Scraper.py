"""
This is the main scraper class, an "abstract" (not via abc library currently), that all the scrapers will inherit from.
"""
from typing import NamedTuple

"""
I KNOW THERE ARE ALOT OF IMPORTS, DO NOT REMOVE ANY, SOME SCRAPERS USE ONE THAT THE REST DON'T!
"""
from abc import ABC, abstractproperty, abstractmethod
from urllib.request import urlopen
from urllib import error
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
import time
import requests
import json
from webdriver_manager.chrome import ChromeDriverManager
from Scrapers.PositionClass import PositionClass

HTML_PARSER = 'html.parser'


class Scraper(ABC):
    """
    The main Scraper 'abstract' class
    """

    def __init__(self):
        """
        initialize a new scraper that has a default Positions list that is of type:
        _company_positions = (Position_object1, ...)
        where Position_object is Position object type that is of the following:

        Position(title= '', company=defaulted to the scrapers self.name, link=defaulted to the scrapers self.url)

        Please consider the objects defaults!
        """
        self._company_positions = []
        self.pos_class = PositionClass(
            defaults=(None, self.name, self.url, self.location, False, None, None, FULLTIME_JOB, None, None))
        self.Position = self.pos_class.create_position

    @abstractmethod
    def scrape(self):
        """
        this should be implemented by each scraper
        :return:
        """
        raise NotImplementedError("No scraper was implemented!")

    def get_positions(self):
        """
        :return: the list of _company_positions that had been(or not) scraped
        """
        return self._company_positions

    """
    Two static methods for the scraping to be just few lines less:
    1. selenium_url_maker
    2. scraping_unit
    """

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
        # try:
        #     driver = webdriver.Chrome(options=chrome_options)
        # except SessionNotCreatedException:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.get(url)
        return driver

    @staticmethod
    def scraping_unit(page_url):
        """
        This is my favorite one, using the BeautifulSoup library, fast and efficient scraper.
        This method creates the yummy soup!
        :param page_url: the url we want to scrape.
        :return: returns the yummy soup!!!
        """
        try:
            # trying to create the page using the urlopen command then the soup <3
            page = urlopen(page_url)
            soup = BeautifulSoup(page, HTML_PARSER)

        # exceptions are really simple, either 404, ssl certificate, or url error, the exceptions should be handled ok
        except error.HTTPError as e:
            if e.code == 404:
                return
            headers = [('User-Agent', 'Mozilla/5.0')]
            opener = build_opener()
            opener.addheaders = headers
            page = opener.open(page_url)
            soup = BeautifulSoup(page, HTML_PARSER)
        except ssl.CertificateError:
            ssl.match_hostname = lambda cert, hostname: True
            page = urlopen(page_url)
            soup = BeautifulSoup(page, HTML_PARSER)
        except error.URLError:
            context = ssl._create_unverified_context()
            page = urlopen(page_url, context=context)
            soup = BeautifulSoup(page, HTML_PARSER)
        # give it to me <3
        return soup

    def check_self(self):
        self.scrape()
        print(f"found {len(self._company_positions)} jobs")
        for pos in self._company_positions:
            print(pos)
