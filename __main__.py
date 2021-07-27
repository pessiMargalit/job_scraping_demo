from ScrapersFactory import ScrapersFactory

if __name__ == '__main__':
    factory = ScrapersFactory()
    factory.start()
    all_positions = factory.get_all_positions()
    for position in all_positions:
        print(position)

