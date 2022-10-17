"""
https://youtu.be/oka2Z05bsuc?t=391
"""


def convert_email_1(email: str) -> str:
    email = email.lower()
    user_name, domain = email.split('@')
    return f'{user_name}@ya.ru' if domain == 'yandex.ru' else email


assert convert_email_1('yandex@yandex.ru') == 'yandex@ya.ru'
assert convert_email_1('yandex.ru@gmail.com') == 'yandex.ru@gmail.com'
assert convert_email_1('yandex.ru@ya.ru') == 'yandex.ru@ya.ru'
assert convert_email_1('google@gmail.com') == 'google@gmail.com'
assert convert_email_1('worker@yandex-team.ru') == 'worker@yandex-team.ru'


def convert_email_2(email: str) -> str:
    email = email.lower().replace('@yandex.ru', '@ya.ru')
    return email


assert convert_email_2('yandex@yandex.ru') == 'yandex@ya.ru'
assert convert_email_2('yandex.ru@gmail.com') == 'yandex.ru@gmail.com'
assert convert_email_2('yandex.ru@ya.ru') == 'yandex.ru@ya.ru'
assert convert_email_2('google@gmail.com') == 'google@gmail.com'
assert convert_email_2('worker@yandex-team.ru') == 'worker@yandex-team.ru'

print('Done')
