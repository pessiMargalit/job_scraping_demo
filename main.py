import sys
import logging
from Scrapers.PositionClass import PositionClass
from ScrapersFactory import ScrapersFactory

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

    logger = logging.getLogger(__name__)
    factory = ScrapersFactory()
    factory.start()
    all_positions = factory.get_all_positions()
    from Publishers.TelegramBotPublisher import *
    if len(sys.argv) > 1 and os.environ.get('DEBUG_FLAG') == sys.argv[1]:
        run_telegram_bot_main(debugging=True)
    else:
        run_telegram_bot_main()

