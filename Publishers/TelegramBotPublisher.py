import os
import logging
from Scrapers.PositionClass import PositionClass
from telegram import ParseMode, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
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
    if not context.args:
        positions_to_post = scraper.get_positions()
    else:
        positions_to_post = list(filter(lambda j:
                                        all(s for s in context.args[0].split(',')
                                            if s in PositionClass.tagging_helper(j)),
                                        scraper.get_positions()))
    if len(positions_to_post) == 0:
        context.bot.send_message(
            text="Oh no! no jobs found :(",
            chat_id=update.message.chat_id
        )
    elif len(positions_to_post) < 5:
        for job in positions_to_post:
            context.bot.send_message(
                text=PositionClass.telegram_repr(job),
                chat_id=update.message.chat_id,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=False,
            )
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=name, callback_data=name) for name
                                                          in ['=>']]])
        context.bot.send_message(chat_id=update.message.chat_id, text='', reply_markup=keyboard)


def run_telegram_bot_main(deubugging=False) -> None:
    if deubugging:
        updater = Updater(os.environ['DEV_BOT_TOKEN'])
    else:
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
