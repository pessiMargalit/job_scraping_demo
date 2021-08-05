import sys

from Scrapers.PositionClass import PositionClass
from ScrapersFactory import ScrapersFactory

if __name__ == '__main__':
    factory = ScrapersFactory()
    factory.start()
    all_positions = factory.get_all_positions()
    # for position in all_positions:
    #     print(PositionClass.telegram_repr(position))
    from Publishers.TelegramBotPublisher import *
    if sys.argv[1] and os.environ.get('DEBUG_FLAG') == sys.argv[1]:
        run_telegram_bot_main(deubugging=True)
    else:
        run_telegram_bot_main()

