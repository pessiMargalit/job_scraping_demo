import os

from Scrapers.PositionClass import PositionClass
from telegram import ParseMode, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram_bot_pagination import InlineKeyboardPaginator
from ScrapersFactory import ScrapersFactory
from Scrapers.CompanyScrapers.LightricksScraper import LightricksScraper
from Scrapers.CompanyScrapers.SimilarWebScraper import SimilarWebScraper
from Scrapers.CompanyScrapers.FacebookScraper import FacebookScraper
from datetime import datetime

BOT_TOKEN = os.environ['BOT_TOKEN']


class JobsTelegramBot:
    def __init__(self, debugging=False):
        self.__positions_to_post = []
        self.__positions = []
        self.last_scrape = datetime.now()

        self.get_jobs()

        if debugging:
            updater = Updater(os.environ['DEV_BOT_TOKEN'])
        else:
            updater = Updater(BOT_TOKEN, use_context=True)
        # Get the dispatcher to register handlers
        self._dispatcher = updater.dispatcher
        self._dispatcher.add_handler(CommandHandler('start', self.start_cmd))
        self._dispatcher.add_handler(CommandHandler('lightricks', self.get_lightricks_jobs))
        self._dispatcher.add_handler(CommandHandler('similarweb', self.get_similarweb_jobs))
        self._dispatcher.add_handler(CommandHandler('facebook', self.get_facebook_jobs))
        self._dispatcher.add_handler(CallbackQueryHandler(self.positions_page_callback, pattern='^Positions#'))

        # Start the Bot
        updater.start_polling()

        # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
        # SIGABRT. This should be used most of the time, since start_polling() is
        # non-blocking and will stop the bot gracefully.
        updater.idle()

    def get_jobs(self):
        fc = ScrapersFactory()
        fc.start()
        self.__positions = fc.get_all_positions()

    def refresh_jobs(self):
        self.last_scrape = datetime.now()
        self.get_jobs()

    def check_if_needs_refresh(self):
        if (self.last_scrape - datetime.now()).days > 0:
            self.refresh_jobs()

    @staticmethod
    def start_cmd(update: Update, context: CallbackContext) -> None:
        context.bot.send_message(
            update.message.chat_id,
            f"Hi! I'm a demo job board bot, select one of the options below and check me out 🤩",
        )

    @staticmethod
    def post_might_take_awhile_message(update: Update, context: CallbackContext):
        context.bot.send_message(
            update.message.chat_id,
            f"Running... this might take some time 😅",
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=False
        )

    def get_lightricks_jobs(self, update: Update, context: CallbackContext) -> None:
        self.check_if_needs_refresh()
        self.__positions_to_post = list(filter(lambda p: p.company is LightricksScraper.name, self.__positions))
        self.post_positions(update=update, context=context)

    def get_similarweb_jobs(self, update: Update, context: CallbackContext) -> None:
        self.check_if_needs_refresh()
        self.__positions_to_post = list(filter(lambda p: p.company is SimilarWebScraper.name, self.__positions))
        self.post_positions(update=update, context=context)

    def get_facebook_jobs(self, update: Update, context: CallbackContext) -> None:
        self.check_if_needs_refresh()
        self.__positions_to_post = list(filter(lambda p: p.company is FacebookScraper.name, self.__positions))
        self.post_positions(update=update, context=context)

    def post_positions(self, update: Update, context: CallbackContext) -> None:
        if context.args:
            search_words = [q.strip() for q in ' '.join(context.args).split(',')]
            self.__positions_to_post = list(filter(lambda j:
                                                   any(s for s in search_words if s in PositionClass.tagging_helper(j)),
                                                   self.__positions_to_post))
        if len(self.__positions_to_post) == 0:
            context.bot.send_message(
                text="Oh no! no jobs found :(",
                chat_id=update.message.chat_id
            )
        else:
            paginator = InlineKeyboardPaginator(
                len(self.__positions_to_post),
                data_pattern="Positions#{page}",
            )
            update.message.reply_text(
                text=PositionClass.telegram_repr(self.__positions_to_post[0]),
                reply_markup=paginator.markup,
                parse_mode=ParseMode.HTML
            )

    def positions_page_callback(self, update, context):
        query = update.callback_query

        query.answer()

        page = int(query.data.split('#')[1])

        paginator = InlineKeyboardPaginator(
            len(self.__positions_to_post),
            current_page=page,
            data_pattern="Positions#{page}",
        )

        query.edit_message_text(
            text=PositionClass.telegram_repr(self.__positions_to_post[page - 1]),
            reply_markup=paginator.markup,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=False,
        )


def run_telegram_bot_main(debugging=False):
    JobsTelegramBot(debugging=debugging)
