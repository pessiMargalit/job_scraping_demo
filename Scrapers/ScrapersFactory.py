import logging
import warnings
from threading import Thread
from queue import Queue
import time
from Scrapers import Scraper
from Scrapers.MainScrapers import *

MAX_WORKERS = 21  # N + 1


class ScraperWorker(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            scraper = self.queue.get()
            try:
                logging.debug(f"Current Company: {scraper.name}")
                scraper.scrape()
            except Exception as e:
                logging.error(f"Scraper for: {scraper.name}, is broken with error: {str(e)}")
                warnings.warn(str(e))
            finally:
                self.queue.task_done()


class ScrapersFactory:
    def __init__(self):
        self.positions = []
        self.no_position_companies = []
        self.timing_dictionary = {}
        self.banned = ['Sivan Innovation', 'Survey Monkey', 'Kaltura', 'Coders Clan', 'Parsempo',
                       'Kaholo', 'Austrade', 'C2A', 'IDT', 'HUJI Innovate', ' Blink.gg',
                       'Vinciworks', 'Silverbolt', 'Mixtiles', 'Merck', 'Taboola', 'Carmel6000',
                       'Revelator', 'Ericom', 'Genetika+', 'Sixdof.Space', 'Miggo', 'Protego',
                       'Rybtech', 'Auth0', 'Dribbble', 'Herolo', '40Nuggets', 'John Bryce',
                       'Quality Score', 'Mellanox']
        # self.main_scrapers = [GovilScraper.GovIlMainScraper.__name__,
        #                       GreenhouseMainScraper.GreenhouseMainScraper.__name__,
        #                       ComeetScraper.ComeetMainScraper.__name__, LeverScraper.LeverMainScraper.__name__,
        #                       WorkableScraper.WorkableMainScraper.__name__, WorkdayScraper.WorkdayMainScraper.__name__,
        #                       WorkdayExternalScraper.WorkdayExternalMainScraper.__name__,
        #                       JobviteScraper.JobviteMainScraper.__name__, UltiproScraper.UltiproMainScraper.__name__,
        #                       BambooHRScraper.BambooHRMainScraper.__name__]
        self.manual_boards = ['TechSparkManual', 'MuniManual']

    def __all_subclasses(self, cls):
        return set(cls.__subclasses__()).union(s for c in cls.__subclasses__() for s in self.__all_subclasses(c))

    def start(self, should_run=True, only_companies=[]):
        self.all_scrapers = [cls() for cls in Scraper.Scraper.__subclasses__()
                             if cls.name not in self.banned and (not only_companies or cls.name in only_companies)]
        if should_run:
            self.timing_dictionary = {k.name: 0 for k in self.all_scrapers}
            self.__parallel_run(self.all_scrapers, self.positions)

    def __parallel_run(self, scrapers, to_write_to):
        queue = Queue()
        ts = time.time()
        for _ in range(MAX_WORKERS):
            worker = ScraperWorker(queue)
            worker.daemon = True
            worker.start()
        for scraper in scrapers:
            queue.put(scraper)
        queue.join()
        for scraper in scrapers:
            if not scraper.positions:
                self.no_position_companies.append(scraper.name)
            to_write_to += scraper.positions
        te = time.time()
        logging.info(f"Finished parallel run in: {te - ts:.2f} s")
        logging.info(f"Total jobs: {len(to_write_to)}")

    def get_zero_pos_companies(self):
        return self.no_position_companies

    def get_scrapers_names(self):
        return [cls.name for cls in self.__all_subclasses(Scraper.Scraper) if cls.name not in self.banned]

    def get_all_scrapers(self):
        return [cls() for cls in self.__all_subclasses(Scraper.Scraper) if cls.name not in self.banned]

    def get_worst_timers(self):
        return dict(
            sorted(filter(lambda elem: elem[1] >= 100, self.timing_dictionary.items()), key=lambda elem: elem[1],
                   reverse=True))

    def get_scraper_by_name(self, scraper_name):
        scrapers = [cls() for cls in self.__all_subclasses(Scraper.Scraper)
                    if cls.name.lower() == scraper_name.lower()]
        # if any([s.name in self.main_scrapers for s in scrapers]):
        #     return []
        return scrapers

    def get_scraper_by_filename(self, filename):
        filename_without_extension = filename.replace('.py', '')
        scrapers = [cls for cls in self.__all_subclasses(Scraper.Scraper) if filename_without_extension in cls.__name__]
        if scrapers:
            return scrapers[0]()
