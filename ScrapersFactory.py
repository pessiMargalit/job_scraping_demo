import warnings, logging

from Scrapers import *
from Scrapers.CompanyScrapers import *
import Scrapers

import time
from tqdm import tqdm


class ScrapersFactory:
    """
    This class is a factory class that creates all the scrapers from the scrapers folder then runs them thus creating
    the data structure needed
    """
    show_runtimes = False
    use_banned = True
    debug_enabled = False

    def __init__(self):
        # create a list of instantiated classes for every scraper inheritance (a company scraper)
        self.all_scrapers = [cls() for cls in Scraper.Scraper.__subclasses__()]
        self.__positions = []
        self.__timing_dictionary = {}

    def start(self):
        self.__timing_dictionary = {k.name: 0 for k in self.all_scrapers}
        self.__run(self.all_scrapers)

    def __run(self, scrapers):
        """
        this function is a private function that runs the scrapers created in the init function
        :param scrapers: list of Scraper() objects given from the init method
        """
        # scrapers = [cls() for cls in Scraper.Scraper.__subclasses__()]
        for scraper in tqdm(scrapers, desc="Running scrapers", disable=not self.debug_enabled):
            logging.debug("Current Company: " + scraper.name)
            ts = time.time()
            try:
                scraper.scrape()

                te = time.time()
                if self.show_runtimes:
                    logging.debug('%r  %2.2f s' % (scraper.name, (te - ts)))
                self.__timing_dictionary[scraper.name] = (te - ts)
            except Exception as e:
                logging.error("Scraper for:" + scraper.name + ", is broken with error: " + e.__str__())
                te = time.time()
                if self.show_runtimes:
                    logging.debug('%r  %2.2f s' % (scraper.name, (te - ts)))
                self.__timing_dictionary[scraper.name] = (te - ts)
                warnings.warn(e.__str__())
                continue
            self.__positions += scraper.get_positions()

    def get_scrapers_names(self):
        return [cls.name for cls in Scraper.Scraper.__subclasses__() if cls.name not in self.banned]

    def get_worst_timers(self):
        return dict(
            sorted(filter(lambda elem: elem[1] >= 100, self.__timing_dictionary.items()), key=lambda elem: elem[1],
                   reverse=True))

    def get_all_positions(self):
        return self.__positions
