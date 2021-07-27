import os
import logging
from Scrapers.PositionClass import PositionClass
from telegram import ParseMode, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from Scrapers.CompanyScrapers.LightricksScraper import LightricksScraper
from Scrapers.CompanyScrapers.FacebookScraper import FacebookScraper
from Scrapers.CompanyScrapers.MicrosoftScraper import MicrosoftScraper

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ['BOT_TOKEN']


# GROUP_ID = int(os.environ['JOBS_WEEKLY'])


def get_lightricks_jobs(update: Update, context: CallbackContext) -> None:
    post_might_take_awhile_message(update, context)
    scraper = LightricksScraper()
    scraper.scrape()
    post_positions(scraper, update, context)

def get_facebook_jobs(update: Update, context: CallbackContext) -> None:
    post_might_take_awhile_message(update, context)
    scraper = FacebookScraper()
    scraper.scrape()
    post_positions(scraper, update, context)

def get_microsoft_jobs(update: Update, context: CallbackContext) -> None:
    post_might_take_awhile_message(update, context)
    scraper = MicrosoftScraper()
    scraper.scrape()
    post_positions(scraper, update, context)


def post_might_take_awhile_message(update: Update, context: CallbackContext):
    context.bot.send_message(
        update.message.chat_id,
        f"Running... this might take some time 😅",
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False
    )


def post_positions(scraper, update: Update, context: CallbackContext) -> None:
    for job in scraper.get_positions():
        message = PositionClass.telegram_repr(job)
        if not context.args:
            context.bot.send_message(
                text=message,
                chat_id=update.message.chat_id,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True
            )
        elif any(s for s in context.args[0].split(',') if s in PositionClass.tagging_helper(job)):
            context.bot.send_message(
                text=message,
                chat_id=update.message.chat_id,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True
            )


def run_telegram_bot_main() -> None:
    updater = Updater(BOT_TOKEN)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    from datetime import datetime
    dispatcher.add_handler(CommandHandler('lightricks', get_lightricks_jobs))
    dispatcher.add_handler(CommandHandler('microsoft', get_microsoft_jobs))
    dispatcher.add_handler(CommandHandler('facebook', get_facebook_jobs))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()
