from Maintainer import *
from WhatsAppBot import *


if __name__ == '__main__':
    while True:
        Maintainer.update_table()
        Table = Maintainer.open_table()
        persons, phones = Maintainer.find_soon_day_birthday(Table)
        for person in persons:
            WhatsAppBot.send_message(f'⚡ Через *два* дня день рождения у:\n*{person}*', (..., ...))
        time.sleep(86_400)
