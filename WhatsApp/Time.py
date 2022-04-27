from datetime import datetime, timedelta


class Time(object):
    @staticmethod
    def timedelta(day: int, month: int, year: int):
        return Time.datetime_to_delta(datetime(year=year, month=month, day=day))

    @staticmethod
    def datetime_to_delta(date: datetime):
        return timedelta(days=date.year * 365 + date.month * 30 + date.day)

    @staticmethod
    def current_datetime(type: str = 'timedelta') -> datetime:
        date = datetime.now()
        if type == 'datetime':
            return date
        elif type == 'timedelta':
            return Time.datetime_to_delta(date)
        return TypeError(f'Incorrect type {type}')

    @staticmethod
    def current_str_date() -> datetime.strftime:
        return datetime.now().strftime("%Y.%m.%d")

    @staticmethod
    def is_soon(today: timedelta, birthday: timedelta) -> bool:
        difference: timedelta = today.days - birthday.days
        return difference % 365 == 364
