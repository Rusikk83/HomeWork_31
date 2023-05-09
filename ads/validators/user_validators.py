import datetime

from rest_framework.exceptions import ValidationError

def check_birth_date(birth_date):
    today = datetime.date.today()
    max_date_birth = today.replace(year=(today.year - 9))

    if max_date_birth < birth_date:
        raise ValidationError('Пользователям младше 9 лет регистрироваться запрещено')


def check_email(email):
    if 'rambler.ru' in email:
        raise ValidationError ("Нельзя использовать email в домене rambler.ru")

