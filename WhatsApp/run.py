from Maintainer import *
from WhatsAppBot import *


if __name__ == '__main__':
    while True:
        # Maintainer.update_table()
        Table = Maintainer.open_table()
        persons, phones = Maintainer.find_soon_day_birthday(Table)
        print(phones)
        for person in persons:
            with open('WAB_logs.out', 'a', encoding='utf-8') as output:
                print(WhatsAppBot.send_message(
                    f'⚡ *Завтра* день рождения у:\n_{person}_ 🥳', ('7 977 700-88-13',)),
                    file=output
                )
        time.sleep(86_400)  # 1 day :)
