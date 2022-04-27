from Maintainer import *
from WhatsAppBot import *


if __name__ == '__main__':
    """Infinite cycle where we check soonest birthdays and send notification about them to anyone you want"""
    while True:
        # Maintainer.update_table(path='here your path', url='here your url for downloading .xlsx table')
        Table = Maintainer.open_table(path='here your path')  # Reading table
        persons, phones = Maintainer.find_soon_day_birthday(Table)
        for person in persons:  # Send notification about each person in persons
            with open('WhatsAppBot_logs.out', 'a', encoding='utf-8') as output:
                """If you don't have access to WhatsApp API, you may use .send_message_manual"""
                for phone in phones:
                    print(WhatsAppBot.send_message(  # You may edit message you need to send
                        f'⚡ *Завтра* день рождения у:\n_{person}_ 🥳', phone),
                        file=output
                    )
        time.sleep(86_400)  # 1 day :)
