if __name__ != '__main__':
    """
                        -------------------------------------------------------
                        | DOCUMENTATION LANGUAGE  || RU & ENG   		      |
                        | Created by Nps-rf 	  || 25.04.2022		          |
                        | Edited by Nps-rf	      || 28.04.2022			      |
                        | Email				      || Divine.Nikolai@Gmail.com |
                        -------------------------------------------------------
    """
else:
    from Maintainer import *
    from WhatsAppBot import *
    """Infinite cycle where we check soonest birthdays and send notification about them to anyone you want"""
    while True:
        Maintainer.update_table(path='here your path', url='here your url for downloading .xlsx table')
        Table = Maintainer.open_table()  # Reading table
        persons, phones = Maintainer.find_soon_day_birthday(Table)
        for person in persons:  # Send notification about each person in persons
            with open('WhatsAppBot_logs.out', 'a', encoding='utf-8') as output:
                """If you don't have access to WhatsApp API, you may use .send_message_manually"""
                for phone in phones:
                    print(WhatsAppBot.send_message(  # You may edit message you need to send
                        f'⚡ *{person[1]}* день рождения у:\n_{person[0]}_ 🥳', phone),
                        file=output
                    )
        time.sleep(86_400)  # Your Timeout, i guess 1 day is more than enough.
